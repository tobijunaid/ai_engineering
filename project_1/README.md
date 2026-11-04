# Small-Business Inventory and Invoicing API

A RESTful API for managing products, inventory, customers, invoices, and payments for small businesses.

## 1. Project Overview

The Small-Business Inventory and Invoicing API is a backend application designed to help small businesses manage their day-to-day sales and inventory operations from one centralized system.

It allows business owners and authorized staff to manage products, monitor stock levels, maintain customer records, generate invoices, and track payments.

The application will be built with **FastAPI, PostgreSQL, SQLAlchemy 2.0, and Pydantic v2**, following practices that support security, maintainability, scalability, and automated testing.

## 2. Problem Statement

Many small businesses rely on manual records, spreadsheets, or disconnected applications to manage inventory and sales.

These approaches can result in:

- Inaccurate stock records.
- Difficulty tracking products sold and remaining quantities.
- Poor visibility into unpaid or partially paid invoices.
- Disorganized customer and transaction records.
- Limited accountability when inventory changes.

This project aims to address these challenges through a centralized API that manages inventory and invoicing while maintaining accurate and traceable business records.

## 3. Project Goals

The project aims to:

- Provide secure user authentication and authorization.
- Allow businesses to manage products and customers.
- Track current inventory quantities.
- Maintain a history of stock movements.
- Create, confirm, and void invoices.
- Support full and partial customer payments.
- Calculate outstanding invoice balances.
- Maintain accurate transaction records.
- Provide comprehensive API documentation.
- Implement automated tests and a repeatable deployment process.

## 4. MVP Scope

The first version will contain six core modules.

### 4.1 Authentication and Users

- User registration and login.
- JWT-based authentication.
- Access and refresh token support.
- Business owner and staff roles.
- Role-based access control.

### 4.2 Products

- Create products.
- Retrieve individual products and product lists.
- Update product information.
- Delete or deactivate products.
- Store product names, descriptions, prices, and stock information.

### 4.3 Inventory

- Track available stock quantities.
- Record stock additions and reductions.
- Record stock movements caused by sales.
- Record damaged, returned, or manually adjusted stock.
- Maintain a historical record of inventory changes.

### 4.4 Customers

- Create customer records.
- Retrieve customer information.
- Update customer details.
- View customer invoice history.
- Store basic contact information.

### 4.5 Invoices

- Create draft invoices.
- Add one or more products to an invoice.
- Confirm invoices.
- Void confirmed invoices.
- Calculate invoice totals.
- Track invoice payment status.

### 4.6 Payments

- Record customer payments.
- Support full and partial payments.
- Calculate outstanding balances.
- Maintain payment transaction history.
- Update invoice payment status.

## 5. User Roles and Permissions

The system will initially support two roles.

| Action                   | Business Owner | Staff Member               |
| ------------------------ | -------------- | -------------------------- |
| View business records    | Yes            | Yes                        |
| Manage products          | Yes            | Yes, subject to permission |
| Manage inventory         | Yes            | Yes, subject to permission |
| Manage customers         | Yes            | Yes                        |
| Create invoices          | Yes            | Yes                        |
| Confirm invoices         | Yes            | Yes, subject to permission |
| Void invoices            | Yes            | No                         |
| Record payments          | Yes            | Yes                        |
| Manage staff accounts    | Yes            | No                         |
| Manage business settings | Yes            | No                         |

All users must be authenticated before accessing protected resources. Staff permissions will be enforced by the API rather than relying on frontend restrictions.

## 6. Business Rules

These rules define how the application should behave.

### 6.1 Inventory Rules

- Creating a draft invoice does not reduce available stock.
- Confirming an invoice reduces stock by the quantities listed in its invoice items.
- An invoice cannot be confirmed if there is insufficient stock.
- Every stock change must generate a stock movement record.
- Stock movements must retain their reason, quantity, timestamp, and associated transaction where applicable.

### 6.2 Invoice Rules

- An invoice can contain one or more products.
- Invoices begin in the draft state.
- Confirming an invoice makes it an official transaction and reduces stock.
- Confirmed invoices cannot be freely edited.
- If a confirmed invoice is incorrect, it must be voided and a corrected invoice created.
- Voiding an invoice restores the stock previously deducted, where applicable.
- Original invoice records and cancellation details must remain available for auditing.

### 6.3 Payment Rules

- An invoice can be unpaid, partially paid, or paid.
- Customers can make multiple payments against one invoice.
- Total payments must not exceed the outstanding invoice balance.
- The outstanding balance is calculated from the invoice total minus recorded payments.
- Recording a payment updates the invoice's payment status.
- Payments must remain traceable through transaction records.

### 6.4 Business Ownership Rules

- Each business's records must be isolated from other businesses.
- Users can only access records belonging to their business, subject to their permissions.
- A business owner controls staff access and business settings.

## 7. API Resource and Endpoint Outline

All endpoints will be prefixed with `/api/v1`.

| Resource       | Method | Endpoint                          | Purpose                             |
| -------------- | ------ | --------------------------------- | ----------------------------------- |
| Authentication | POST   | `/auth/register`                  | Register a user and business        |
| Authentication | POST   | `/auth/login`                     | Authenticate a user                 |
| Authentication | POST   | `/auth/refresh`                   | Refresh access token                |
| Authentication | POST   | `/auth/logout`                    | Log out or revoke a refresh session |
| Users          | GET    | `/users/me`                       | Retrieve current user               |
| Users          | GET    | `/users`                          | List business users                 |
| Users          | POST   | `/users`                          | Add a staff member                  |
| Products       | POST   | `/products`                       | Create a product                    |
| Products       | GET    | `/products`                       | List products                       |
| Products       | GET    | `/products/{product_id}`          | Retrieve a product                  |
| Products       | PATCH  | `/products/{product_id}`          | Update a product                    |
| Products       | DELETE | `/products/{product_id}`          | Deactivate or delete a product      |
| Inventory      | GET    | `/inventory`                      | View inventory                      |
| Inventory      | GET    | `/inventory/movements`            | View stock movement history         |
| Inventory      | POST   | `/inventory/adjustments`          | Record a stock adjustment           |
| Customers      | POST   | `/customers`                      | Create a customer                   |
| Customers      | GET    | `/customers`                      | List customers                      |
| Customers      | GET    | `/customers/{customer_id}`        | Retrieve a customer                 |
| Customers      | PATCH  | `/customers/{customer_id}`        | Update a customer                   |
| Invoices       | POST   | `/invoices`                       | Create a draft invoice              |
| Invoices       | GET    | `/invoices`                       | List invoices                       |
| Invoices       | GET    | `/invoices/{invoice_id}`          | Retrieve an invoice                 |
| Invoices       | POST   | `/invoices/{invoice_id}/confirm`  | Confirm an invoice                  |
| Invoices       | POST   | `/invoices/{invoice_id}/void`     | Void an invoice                     |
| Payments       | POST   | `/invoices/{invoice_id}/payments` | Record a payment                    |
| Payments       | GET    | `/invoices/{invoice_id}/payments` | List invoice payments               |

The endpoint list is an initial design. Request schemas, response formats, filtering, pagination, and exact status codes will be defined during implementation.

## 8. Technology Stack

| Technology        | Purpose                                       |
| ----------------- | --------------------------------------------- |
| Python            | Main programming language                     |
| FastAPI           | REST API framework                            |
| Pydantic v2       | Request validation and response schemas       |
| PostgreSQL        | Relational database                           |
| SQLAlchemy 2.0    | ORM and database interaction                  |
| Alembic           | Database migrations                           |
| JWT               | Authentication and token-based access         |
| Redis             | Rate limiting and supporting cache operations |
| Pytest            | Automated testing                             |
| HTTPX             | API testing                                   |
| Docker            | Application containerization                  |
| Git and GitHub    | Version control and collaboration             |
| GitHub Actions    | Continuous integration                        |
| Railway or Fly.io | Deployment                                    |

## 9. Architecture Overview

The application will use a modular layered architecture.

### Main Components

**API Layer**

- Defines HTTP endpoints.
- Handles incoming requests.
- Applies authentication and authorization.
- Returns appropriate HTTP responses.

**Schema Layer**

- Defines request and response structures.
- Validates incoming data using Pydantic.
- Ensures consistent API responses.

**Service Layer**

- Contains business logic.
- Handles invoice confirmation, stock adjustments, and payment processing.
- Coordinates operations across different modules.

**Database Layer**

- Defines SQLAlchemy models.
- Handles database queries and transactions.
- Manages relationships and constraints.

**Migration Layer**

- Uses Alembic to track database schema changes.
- Allows database changes to be applied and reversed in a controlled way.

### Request Flow

Client → FastAPI Router → Authentication/Validation → Service Layer → SQLAlchemy → PostgreSQL → API Response

Business operations that modify multiple records, such as confirming an invoice, must use database transactions to prevent inconsistent records.

## 10. Database Design

The initial database is expected to contain the following entities:

| Entity                    | Responsibility                                       |
| ------------------------- | ---------------------------------------------------- |
| Businesses                | Stores business information                          |
| Users                     | Stores user accounts and roles                       |
| Products                  | Stores product details                               |
| Inventory Movements       | Records stock additions, reductions, and adjustments |
| Customers                 | Stores customer information                          |
| Invoices                  | Stores invoice-level information                     |
| Invoice Items             | Stores products and quantities belonging to invoices |
| Payments                  | Stores payments made against invoices                |
| Refresh Tokens / Sessions | Supports refresh-token management and revocation     |

The detailed database schema will define:

- Primary and foreign keys.
- Field types and validation constraints.
- One-to-many and other table relationships.
- Unique constraints and indexes.
- Appropriate deletion and archival behaviour.
- Transactional requirements.

Invoice items should preserve the product description and unit price at the time of invoicing so that later product changes do not alter historical invoices.

## 11. Security and Reliability

The application will incorporate:

- Password hashing rather than storing plain-text passwords.
- JWT access and refresh token handling.
- Role-based authorization.
- Business-level data isolation.
- Request validation.
- Rate limiting using Redis.
- Environment variables for sensitive configuration.
- Structured application logging.
- Database transactions for critical operations.
- Consistent error handling.

## 12. Testing Strategy

Automated testing will be implemented using Pytest and HTTPX.

Testing will cover:

- User registration and login.
- Authentication and authorization.
- Product CRUD operations.
- Inventory adjustments and movement history.
- Customer management.
- Invoice creation and confirmation.
- Insufficient-stock scenarios.
- Invoice cancellation and stock restoration.
- Full and partial payments.
- Invalid payment amounts.
- Business data isolation.

The project will target **more than 80% automated test coverage**.

## 13. Setup and Installation

The exact commands will be finalized when the project structure and configuration are implemented.

Expected setup process:

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install project dependencies.
4. Configure environment variables.
5. Set up the PostgreSQL database.
6. Configure Redis.
7. Apply Alembic migrations.
8. Start the FastAPI development server.

The application will expose interactive API documentation through FastAPI's Swagger UI.

## 14. Deployment and CI/CD

The application will be containerized using Docker.

GitHub Actions will be used to automate checks such as:

- Dependency installation.
- Code quality checks.
- Automated tests.
- Test coverage reporting.

Deployment will be carried out using Railway or Fly.io, with PostgreSQL and Redis configured as supporting services.

Production secrets and database credentials will be managed through environment configuration rather than committed to the repository.

## 15. Future Improvements

Features that may be considered after the MVP include:

- Multiple warehouse locations.
- Supplier and procurement management.
- Low-stock notifications.
- Product categories and variants.
- Advanced sales and financial reports.
- Tax calculations.
- Online payment gateway integration.
- Invoice PDF generation.
- Email notifications.
- Audit logs and business activity reports.

## 16. Project Status

**Current stage:** Requirements and system design.

Implementation will begin after the README and database schema have been reviewed and agreed upon.

---

## License

License to be determined.
