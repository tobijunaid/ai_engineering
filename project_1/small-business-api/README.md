# Small Business Inventory & Invoicing API

A REST API for small businesses to manage **products, inventory, customers, invoices and payments** — the kind of software a shop that outgrew spreadsheets would actually use.

Built as the first project in my AI-engineering build sprint. The focus is on **real engineering** over clever code: a layered architecture, business-rule enforcement at the service layer, database constraints as a backstop, 88 passing tests, and Docker for reproducible local runs.

Design document: [`../design.md`](../design.md) · Overview: [`../README.md`](../README.md)

---

## What it does

- **Authentication.** Business-owner registration, JWT login, owner-managed staff accounts with role-based access control.
- **Products.** Business-scoped CRUD with soft delete. Each product gets an inventory row at quantity 0 on creation.
- **Inventory.** Stock levels + an append-only ledger of movements (`stock_in` / `return` / `damage` / `adjustment` / `sale` / `void_reversal`). Row-locked, so concurrent stock changes can't overdraw.
- **Customers.** CRUD + name/email/phone search + invoice history.
- **Invoices.** Draft → confirm → void lifecycle. Confirming reduces stock atomically (all items or none). Voiding a confirmed invoice restores stock as `void_reversal` movements and records who voided it, when and why.
- **Payments.** Full and partial payments on confirmed invoices. Row-locked to prevent overpayment. `payment_status` progresses `unpaid` → `partially_paid` → `paid`.

Every record is scoped to the authenticated user's `business_id`, so one shop can never see another's data.

---

## Tech stack

Python 3.13 · FastAPI · PostgreSQL 16 · SQLAlchemy 2.0 · Alembic · Pydantic v2 · pytest · Docker

---

## Project layout

```
app/
  api/v1/        HTTP endpoints — one router per module
  core/          config + security (hashing, JWT, dependencies)
  db/            engine, Session, get_db dependency
  models/        SQLAlchemy ORM models
  schemas/       Pydantic request/response schemas
  services/      business logic — the single source of truth for each rule
migrations/      Alembic migrations
tests/           pytest; a fresh schema is built in a dedicated test DB
```

Routers raise HTTP errors; services raise domain exceptions (`ProductNotFoundError`, `InsufficientStockError`, …). The service layer never imports FastAPI.

---

## Run with Docker (easiest)

```bash
docker compose up --build
```

API: `http://localhost:8000` · Docs: `http://localhost:8000/docs` · Postgres: `localhost:5433`

The API container runs `alembic upgrade head` on start, so the schema is ready on first boot. To override defaults, create a `.env` next to `docker-compose.yml`:

```env
POSTGRES_PASSWORD=your-password
SECRET_KEY=your-long-random-string
```

Tear down and wipe the database volume with `docker compose down -v`.

---

## Run locally (no Docker)

**Requires** Python 3.13 and a running PostgreSQL. Create two databases: `small_business_db` and `small_business_test_db`.

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS/Linux
pip install -r requirements.txt

cp .env.example .env            # then fill in SECRET_KEY, DATABASE_URL, TEST_DATABASE_URL
alembic upgrade head
uvicorn app.main:app --reload
```

### Tests

```bash
pytest -q
```

The test suite builds its own schema in `small_business_test_db` and refuses to run against any other name — tests can never touch the dev database.

---

## Endpoint summary

All endpoints live under `/api/v1`. Full request/response shapes are at `/docs` once the app is running.

| Module | Endpoint | Who |
|---|---|---|
| Auth | `POST /auth/register`, `POST /auth/login`, `GET /auth/me` | public / self |
| Auth | `POST /auth/staff`, `GET /auth/staff`, `PATCH /auth/staff/{id}[/deactivate\|/reactivate]` | owner |
| Products | `POST /products`, `GET /products`, `GET/PATCH /products/{id}` | owner, staff |
| Products | `PATCH /products/{id}/[de\|re]activate` | owner |
| Inventory | `GET /inventory`, `GET /inventory/{product_id}` | owner, staff |
| Inventory | `POST /inventory/{product_id}/movements`, `GET .../movements` | owner, staff |
| Inventory | `POST /inventory/{product_id}/adjust` | owner |
| Customers | `POST /customers`, `GET /customers?search=`, `GET/PATCH /customers/{id}` | owner, staff |
| Customers | `GET /customers/{id}/invoices` | owner, staff |
| Invoices | `POST /invoices`, `GET /invoices?status=&customer_id=`, `GET /invoices/{id}` | owner, staff |
| Invoices | `POST/PATCH/DELETE /invoices/{id}/items[/{item_id}]` | owner, staff (draft only) |
| Invoices | `POST /invoices/{id}/confirm` | owner, staff |
| Invoices | `POST /invoices/{id}/void` | owner |
| Payments | `POST /invoices/{id}/payments`, `GET /invoices/{id}/payments` | owner, staff |
| Health | `GET /`, `GET /health/database` | public |

---

## Key design choices

- **Service layer owns the rules.** A router is a thin HTTP translator. This keeps rules testable without a live HTTP client, and makes it obvious where to add logic.
- **Database constraints are a backstop.** `CHECK`, `UNIQUE` and foreign-key constraints catch bugs that slip past the service layer.
- **Inventory is a ledger.** Every movement row carries `quantity_after` — the stock balance after the movement — so history is auditable and the "current stock" row is really a cached running total.
- **Snapshots on invoice items.** Lines copy `product_name` and `unit_price` at the moment they're added. Renaming a product or changing its price never rewrites past invoices.
- **Confirming an invoice is atomic.** Stock changes for every line run in one transaction. If any item is short, the whole confirm rolls back; the invoice stays a draft.
- **Row locks for race conditions.** `SELECT ... FOR UPDATE` on the inventory row, invoice row (during confirm/void/pay) and business row (during invoice numbering).
- **Derived vs stored values.** `amount_paid` and `balance_due` are computed from payments (always correct). `payment_status` is stored (cheap to filter on).
- **Nothing is deleted.** Products are soft-deleted; invoices are voided rather than removed; payments are immutable. Accountants care.

See [`../../SPRINT_TRACKER.md`](../../SPRINT_TRACKER.md) for known limits, tech debt and concepts to revisit.

---

## Status

MVP complete — 88 tests passing. Still to do: README refresh in the parent design doc, GitHub Actions CI, deployment notes.
