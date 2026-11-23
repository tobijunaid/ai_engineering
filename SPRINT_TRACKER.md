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
| Inventory & stock movements | ✅ | ⬜ | ⬜ |
| Customers | ✅ | ⬜ | ⬜ |
| Invoices (draft → confirm → void) | ✅ | ⬜ | ⬜ |
| Payments (full/partial) | ✅ | ⬜ | ⬜ |
| Deployment (Docker, CI) | — | ⬜ | ⬜ |

### Bugs

- [x] **P1** ~~`/health/database` returns HTTP 200 even when the DB is disconnected — monitoring tools would think the app is healthy.~~ Now returns 503.

### Technical debt

- [ ] **P2** `requirements.txt` is UTF-16 encoded (PowerShell `pip freeze >` default). Git treats it as binary, so diffs are unreadable. Regenerate with `pip freeze | Out-File -Encoding utf8 requirements.txt`.
- [ ] **P2** Both `passlib` and `pwdlib` are installed; only `pwdlib` is used. `python-jose` is poorly maintained — consider `PyJWT`.
- [x] **P3** ~~`app/main.py` has duplicate imports.~~
- [ ] **P3** `.coverage` is committed at the repo root (it's a generated file).
- [ ] **P3** Login has no refresh tokens yet (design doc lists "access and refresh token support").
- [ ] **P3** Staff "subject to permission" (design doc §5) isn't implemented — there are only two roles, no fine-grained permissions.
- [ ] **P3** Products list has no pagination (`limit`/`offset`) — fine for a small shop, needed before large catalogues.
- [ ] **P3** Product responses don't include current stock quantity — add when the inventory module lands.
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
| 2026-11-23 | SKU unique per business, not globally | Two shops can both use “RICE-50”. Already enforced by a DB constraint; the service checks first to return a clean 409. |

---

## Project 2 — AI Building Sprint

Starts after Project 1's MVP is complete. (Folder: `AI-Building-Sprint`.)
