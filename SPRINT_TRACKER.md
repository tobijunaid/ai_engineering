# Sprint Tracker

A living record of what's unfinished, what's broken, and what I need to go back and understand properly.
Updated at the end of every feature. Generated code ≠ understanding — the "Revisit" lists are my study plan for Learn2Earn.

**Legend:** `[ ]` open · `[x]` done · **P1** fix soon · **P2** fix before calling the project "done" · **P3** nice to have

---

## Project 1 — Small Business Inventory & Invoicing API

`project_1/small-business-api` · FastAPI · PostgreSQL · SQLAlchemy 2.0 · Alembic · Pydantic v2 · pytest

### Feature status

| Module | Models + migrations | Endpoints | Tests |
| --- | --- | --- | --- |
| Auth & users (owner/staff, JWT) | ✅ | ✅ | ✅ |
| Products (CRUD + soft delete) | ✅ | ✅ | ✅ (14 tests) |
| Inventory & stock movements | ✅ (+ `quantity_after` migration) | ✅ | ✅ (13 tests) |
| Customers (CRUD + search, no delete) | ✅ | ✅ | ✅ (9 tests) |
| Invoices (draft → confirm → void) | ✅ (+ void-audit migration) | ✅ | ✅ (21 tests) |
| Payments (full/partial) | ✅ | ✅ | ✅ (15 tests) |
| Deployment (Docker, CI) | Docker ✅ · CI ✅ | — | — |

### Bugs

- [x] **P1** ~~`/health/database` returns HTTP 200 even when the DB is disconnected — monitoring tools would think the app is healthy.~~ Now returns 503.

- [x] **P1** ~~`PATCH /products/{id}` with `{"name": null}` → 500 crash (DB NOT NULL violation).~~ Fixed with a `reject_null` validator; regression test added.

### Technical debt

- [x] **P2** ~~`requirements.txt` is UTF-16 encoded.~~ Re-encoded to UTF-8 2026-11-23.
- [ ] **P2** Both `passlib` and `pwdlib` are installed; only `pwdlib` is used. `python-jose` is poorly maintained — consider `PyJWT`.
- [x] **P3** ~~`app/main.py` has duplicate imports.~~
- [ ] **P3** `.coverage` is committed at the repo root (it's a generated file).
- [ ] **P3** Login has no refresh tokens yet (design doc lists "access and refresh token support").
- [ ] **P3** Staff "subject to permission" (design doc §5) isn't implemented — there are only two roles, no fine-grained permissions.
- [ ] **P3** Products list has no pagination (`limit`/`offset`) — fine for a small shop, needed before large catalogues.
- [ ] **P3** Product responses don't include stock quantity — use `GET /inventory` for now; could add to `ProductResponse` later (watch out for N+1 queries).
- [x] **P2** ~~Migration `b7c4e1a9f302` (adds `quantity_after`) must be applied to the dev DB.~~ Applied 2026-11-23.
- [ ] **P3** `alembic ... --sql` (offline mode) is broken: `run_migrations_offline()` reads the placeholder URL in `alembic.ini` instead of `settings.database_url`.
- [ ] **P3** Movement history order relies on `created_at`; rows created in one transaction share a timestamp. Fine in production, but a tie-breaker (or `clock_timestamp()`) would make ordering strict.
- [ ] **P3** Manual `return` movements aren't linked to an invoice yet (`reference_id`) — revisit with the invoices module.
- [ ] **P3** No pagination on movement history or customer list.
- [x] **P2** ~~Customer invoice history~~ — `GET /customers/{id}/invoices` added with invoices.
- [x] **P1** ~~Migration `e4f8a2c6d913` (void audit columns + `void_reversal`) must be applied to the dev DB.~~ Applied 2026-11-23.
- [x] **P2** ~~README endpoint table out of date.~~ Parent design README now points to the implementation README for the real table; `small-business-api/README.md` written 2026-11-23.
- [ ] **P3** Invoice numbers are `INV-00001` strings; list ordering sorts them as text, which breaks after 99,999 invoices. Fine for an MVP.
- [ ] **P3** No pagination on invoice list.
- [x] **P3** ~~No GitHub Actions CI yet.~~ Workflow added 2026-11-23: pytest on push/PR with a Postgres service. Fixed rootdir bug (pytest walked to repo-root `.git` instead of project dir) with `pyproject.toml` + `PYTHONPATH`.
- [ ] **P2** A mistaken payment can't be corrected or reversed (no edit/delete/refund), and it also blocks voiding the invoice. Needs a "payment reversal" feature before real use.
- [ ] **P3** An invoice whose total is 0.00 (all items priced at 0) can never become `paid`: payments must be > 0. Could auto-mark it paid on confirm.
- [ ] **P3** `amount_paid` / `balance_due` are calculated in Python by loading all payments. Fine for a few payments per invoice; a SQL `SUM` would scale better for reports.
- [ ] **P3** Prices are snapshotted when an item is added; if a product's price changes before confirmation, the draft keeps the old price. Deliberate (quoted price), but worth a "refresh prices" action later.
- [ ] **P3** Confirm doesn't re-check whether a product was deactivated after being added to the draft.
- [ ] **P3** Invoice-module errors use an `ERROR_STATUS` map + `_run()` helper; products/inventory/customers still use per-endpoint try/except. Consider unifying (e.g. FastAPI exception handlers) — compare both styles first.
- [ ] **P3** Customer search uses `ILIKE '%term%'`, which can't use a normal index — fine for small data; consider `pg_trgm` later.
- [ ] **P3** Customer emails aren't checked for duplicates (deliberate: households may share contact details).
- [ ] **P3** Older auth tests still repeat register/login boilerplate — could use the new `owner_headers` / `staff_headers` fixtures in `conftest.py`.
- [ ] **P3** Untested: the 503 path of `/health/database` (needs a fake broken DB session).
- [ ] **P3** Silence the `StarletteDeprecationWarning` about `httpx` in tests (dependency version issue).

### Revisit & master (concepts used but not yet owned)

- [ ] **FastAPI dependency injection** — `Depends()`, and how `require_role("owner")` returns a function (a closure / function factory).
- [ ] **JWT auth flow** — what's inside a token, signing vs encryption, why `sub` holds the user ID, expiry.
- [ ] **Password hashing** — why hash rather than encrypt; what argon2 does.
- [ ] **SQLAlchemy 2.0** — `Mapped`, `mapped_column`, `relationship`/`back_populates`, `select()` + `db.scalar()`, sessions and `commit`/`refresh`.
- [ ] **Alembic** — what a migration is, autogenerate, upgrade/downgrade, why models and migrations must stay in sync.
- [ ] **Test isolation** — the `conftest.py` transaction + savepoint rollback trick (`join_transaction_mode="create_savepoint"`), and `dependency_overrides`.
- [ ] **Layered architecture** — router (HTTP) → service (business logic) → model (DB). Why services raise `ValueError` and routers translate it into HTTP status codes.
- [ ] **Multi-tenancy** — isolating each business's data by filtering every query on `business_id`.
- [ ] **Pydantic for PATCH** — optional fields + `model_dump(exclude_unset=True)` so only sent fields change.
- [ ] **`Decimal` vs `float` for money** — and why the API returns prices as strings (`"45000.00"`).
- [ ] **Custom exceptions** (`ProductNotFoundError`) vs plain `ValueError` — the product service uses custom ones; auth still uses `ValueError`. Compare both.
- [ ] **`db.flush()` vs `db.commit()`** — getting an ID mid-transaction; product + inventory saved atomically.
- [ ] **pytest fixtures that depend on fixtures** — `staff_headers` uses `owner_headers` uses `client` uses `db_session`.
- [ ] **Ledger pattern** — movements as an append-only history with `quantity_after`; the inventory row is a cached running total.
- [ ] **Row locking** — `SELECT ... FOR UPDATE` (`with_for_update()`) and the race condition it prevents (two sales of the last item).
- [ ] **Transaction boundaries** — why `_apply_stock_change()` does *not* commit, so invoice confirmation can change many products atomically.
- [ ] **SQL joins in SQLAlchemy** — `select(...).join(...)` returning rows rather than ORM objects.
- [ ] **`now()` in PostgreSQL** — returns transaction start time, not wall-clock time.
- [ ] **Alembic by hand** — adding a NOT NULL column to a table that may have rows (temporary `server_default`).
- [ ] **`Literal` types in Pydantic** — restricting a field to allowed values (how `sale` is blocked).
- [ ] **"Optional" vs "nullable" in PATCH schemas** — the null-update bug: `str | None` lets clients send `null`; `field_validator` blocks it for required columns.
- [ ] **Reproduce bugs with a failing test first**, then fix — how the null bug was handled.
- [ ] **`or_()` and `ilike()`** in SQLAlchemy — building search queries.
- [ ] **State machines** — invoice lifecycle draft → confirmed → void, and guarding each transition (`_require_status`).
- [ ] **Atomic multi-row operations** — confirming N items: all stock changes succeed or none do (`rollback`).
- [ ] **Locking for correctness** — invoice row lock on confirm/void (double-click problem); business row lock for invoice numbering.
- [ ] **N+1 queries and `selectinload`** — why the invoice list loads items in one extra query.
- [ ] **Snapshots in invoice items** — why `product_name` / `unit_price` are copied instead of looked up.
- [ ] **ORM cascades** — `cascade="all, delete-orphan"`: removing an item from `invoice.items` deletes the row.
- [ ] **Alembic: changing a CHECK constraint** — drop + recreate; why downgrade can fail when data uses the new value.
- [ ] **`Query(alias=...)`** — the URL name vs the Python name.
- [ ] **Derived vs stored values** — why `amount_paid`/`balance_due` are `@property`s computed from payments rather than columns (single source of truth), while `payment_status` *is* stored (cheap to filter on).
- [ ] **Nested resource URLs** — `/invoices/{invoice_id}/payments` and a path parameter in the router prefix.
- [ ] **`pytest.mark.parametrize`** — one test function, several inputs.
- [ ] **HTTP status codes** — 201 vs 200, 401 vs 403, 404 vs 409, 422.

### Decisions log

| Date | Decision | Why |
| --- | --- | --- |
| — | UUID primary keys | Don't leak record counts; safe to expose in URLs. |
| — | Separate test DB, refuses any other name | Tests can never wipe dev data. |
| 2026-11-23 | Products are soft-deleted (`is_active`), never hard-deleted | Invoices will reference products; deleting rows would break history. |
| 2026-11-23 | Creating a product auto-creates its inventory row at quantity 0; no initial stock field | Every stock change must go through the inventory module so it gets a movement record (rule 6.1). |
| 2026-11-23 | Owners + staff can create/update products; only owners can deactivate | Simple default for “staff: subject to permission”; revisit if fine-grained permissions are added. |
| 2026-11-23 | Another business's product returns 404, not 403 | Don't reveal that the record exists. |
| 2026-11-23 | Movements store `quantity_after` (stock balance after the movement) | `quantity` is always positive, so `adjustment` had no direction. Also makes the history an auditable ledger. Chosen over signed quantities / decrease-only adjustments. |
| 2026-11-23 | No manual `sale` movements | Sales only come from confirmed invoices (rule 6.1). |
| 2026-11-23 | Adjustment takes the counted total (`new_quantity`) + required reason; owner-only | Matches how a stocktake works; rewriting the books needs accountability. |
| 2026-11-23 | One internal `_apply_stock_change()`; it never commits | Single place that enforces "no negative stock" + writes a movement; invoices will reuse it inside one transaction. |
| 2026-11-23 | Customers have no delete endpoint | Not in the design doc; invoices reference customers. Avoids a migration for `is_active`. |
| 2026-11-23 | Customer email/phone/address can be cleared with `null`; `full_name` cannot | Matches which columns are nullable in the DB. |
| 2026-11-23 | Invoices get `voided_at` / `voided_by` / `void_reason` (reason required) | Rule 6.2: cancellation details must stay auditable. |
| 2026-11-23 | Void restores stock with a new `void_reversal` movement type | Keeps cancelled sales distinct from genuine customer returns in the ledger. |
| 2026-11-23 | Invoices with payments cannot be voided (409) | No refunds module; money records never point at a void invoice. |
| 2026-11-23 | Drafts are voided, never deleted | Invoice numbers stay gap-free; nothing is ever lost. |
| 2026-11-23 | Invoice number = `INV-` + per-business count, generated under a business row lock | Simple and gap-free because invoices are never deleted. |
| 2026-11-23 | Owners + staff create/edit/confirm; only owners void | Matches design §5. |
| 2026-11-23 | `total = subtotal` | Tax/discounts are out of scope (README §15). |
| 2026-11-23 | Payments only on confirmed invoices; never above balance (409); invoice row locked while recording | Rule 6.3; locking prevents two simultaneous payments overpaying. |
| 2026-11-23 | `payment_method` limited to cash / bank_transfer / card / mobile_money / other (API-level) | DB column is free text; validation keeps data clean without a migration. |
| 2026-11-23 | `amount_paid` / `balance_due` computed, not stored | Can never drift out of sync with the payment records. |
| 2026-11-23 | Payments are immutable (no edit/delete endpoints) | Not in the design; money records should be append-only. Corrections → future reversal feature. |
| 2026-11-23 | SKU unique per business, not globally | Two shops can both use “RICE-50”. Already enforced by a DB constraint; the service checks first to return a clean 409. |

---

## Project 2 — AI Building Sprint

Starts after Project 1's MVP is complete. (Folder: `AI-Building-Sprint`.)
