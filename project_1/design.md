Design for first two tables. We'll use PostgreSQL and SQLAlchemy 2.0 conventions.

## 1. `businesses` table

Stores information about each registered business.

| Column       | Data type                | Constraints | Purpose                    |
| ------------ | ------------------------ | ----------- | -------------------------- |
| `id`         | UUID                     | Primary key | Unique business identifier |
| `name`       | VARCHAR(150)             | NOT NULL    | Business name              |
| `email`      | VARCHAR(255)             | NULL        | Business contact email     |
| `phone`      | VARCHAR(30)              | NULL        | Business phone number      |
| `address`    | TEXT                     | NULL        | Business address           |
| `created_at` | TIMESTAMP WITH TIME ZONE | NOT NULL    | Creation timestamp         |
| `updated_at` | TIMESTAMP WITH TIME ZONE | NOT NULL    | Last update timestamp      |

## 2. `users` table

Stores business owners and staff members.

| Column            | Data type                | Constraints            | Purpose                       |
| ----------------- | ------------------------ | ---------------------- | ----------------------------- |
| `id`              | UUID                     | Primary key            | Unique user identifier        |
| `business_id`     | UUID                     | Foreign key, NOT NULL  | Business the user belongs to  |
| `full_name`       | VARCHAR(150)             | NOT NULL               | User's full name              |
| `email`           | VARCHAR(255)             | NOT NULL               | Login email                   |
| `hashed_password` | VARCHAR(255)             | NOT NULL               | Securely hashed password      |
| `role`            | VARCHAR(20)              | NOT NULL               | `owner` or `staff`            |
| `is_active`       | BOOLEAN                  | NOT NULL, default TRUE | Whether the account is active |
| `created_at`      | TIMESTAMP WITH TIME ZONE | NOT NULL               | Creation timestamp            |
| `updated_at`      | TIMESTAMP WITH TIME ZONE | NOT NULL               | Last update timestamp         |

Important constraints:

- User emails should be unique within a business.
- Each business must have at least one owner.
- A user belongs to one business in this initial version.
- `business_id` references `businesses.id`.

## 3. Relationship

BUSINESSES

One business record

`id` (PK)

One-to-many (1:N)

USERS

Many users can belong to one business

`business_id` (FK)

For example, Business A can have one owner and five staff members. All six user records reference the same business ID.


## 4. Products table

The `products` table stores the items each business sells.

| Column          | Data type                | Constraints            | Purpose                        |
| --------------- | ------------------------ | ---------------------- | ------------------------------ |
| `id`            | UUID                     | Primary key            | Unique product identifier      |
| `business_id`   | UUID                     | Foreign key, NOT NULL  | Business that owns the product |
| `name`          | VARCHAR(150)             | NOT NULL               | Product name                   |
| `description`   | TEXT                     | NULL                   | Product description            |
| `sku`           | VARCHAR(50)              | NOT NULL               | Stock Keeping Unit             |
| `selling_price` | NUMERIC(12,2)            | NOT NULL               | Current selling price          |
| `is_active`     | BOOLEAN                  | NOT NULL, default TRUE | Product availability           |
| `created_at`    | TIMESTAMP WITH TIME ZONE | NOT NULL               | Creation timestamp             |
| `updated_at`    | TIMESTAMP WITH TIME ZONE | NOT NULL               | Last update timestamp          |

Two important design decisions:

- `business_id` ensures each product belongs to a particular business.
- `sku` should be unique within a business, not necessarily across the entire platform.

## 5. `inventory` table

This table stores the current stock quantity for each product.

| Column       | Data type                | Constraints                    | Purpose                 |
| ------------ | ------------------------ | ------------------------------ | ----------------------- |
| `id`         | UUID                     | Primary key                    | Unique inventory record |
| `product_id` | UUID                     | Foreign key, NOT NULL, UNIQUE  | Associated product      |
| `quantity`   | INTEGER                  | NOT NULL, default 0, CHECK ≥ 0 | Available stock         |
| `updated_at` | TIMESTAMP WITH TIME ZONE | NOT NULL                       | Last stock update       |

Why separate it from products? Product details and inventory levels represent different concerns. Keeping them separate makes inventory operations easier to manage.

Each product will have one inventory record.

## 6. `inventory_movements` table

We'll also maintain a complete history of stock changes.

| Column          | Data type                | Constraints                    | Purpose                                              |
| --------------- | ------------------------ | ------------------------------ | ---------------------------------------------------- |
| `id`            | UUID                     | Primary key                    | Unique movement identifier                           |
| `product_id`    | UUID                     | Foreign key, NOT NULL          | Product affected                                     |
| `business_id`   | UUID                     | Foreign key, NOT NULL          | Owning business                                      |
| `movement_type` | VARCHAR(30)              | NOT NULL                       | `stock_in`, `sale`, `return`, `damage`, `adjustment` |
| `quantity`      | INTEGER                  | NOT NULL, CHECK > 0            | Number of units affected                             |
| `reason`        | TEXT                     | NULL                           | Explanation for movement                             |
| `reference_id`  | UUID                     | NULL                           | Related invoice or transaction                       |
| `created_by`    | UUID                     | Foreign key to users, NOT NULL | User responsible                                     |
| `created_at`    | TIMESTAMP WITH TIME ZONE | NOT NULL                       | Movement timestamp                                   |

The movement type determines whether stock increases or decreases. For example:

- `stock_in`: +20 units
- `sale`: -3 units
- `damage`: -2 units
- `return`: +1 unit

The `inventory.quantity` field stores the current balance, while `inventory_movements` provides the historical record.

## 7. Updated relationship overview

BUSINESSES

PRODUCTS

1:1

INVENTORY

Current quantity

1:N

INVENTORY MOVEMENTS

Stock history

Important implementation rule: Updating the inventory balance and recording its movement must happen within the same database transaction. This prevents the current stock and its history from becoming inconsistent.

Next, we'll design the `customers`, `invoices`, `invoice_items`, and `payments` tables.

Let's finish the remaining database tables.

## 8. `customers` table

Stores customers belonging to each business.

| Column        | Data type    | Constraints           | Purpose             |
| ------------- | ------------ | --------------------- | ------------------- |
| `id`          | UUID         | Primary key           | Customer identifier |
| `business_id` | UUID         | Foreign key, NOT NULL | Owning business     |
| `full_name`   | VARCHAR(150) | NOT NULL              | Customer name       |
| `email`       | VARCHAR(255) | NULL                  | Email address       |
| `phone`       | VARCHAR(30)  | NULL                  | Phone number        |
| `address`     | TEXT         | NULL                  | Customer address    |
| `created_at`  | TIMESTAMPTZ  | NOT NULL              | Creation timestamp  |
| `updated_at`  | TIMESTAMPTZ  | NOT NULL              | Last update         |

A business can have many customers. Customer email and phone should not be globally unique because different businesses may serve the same customer.

## 9. `invoices` table

Stores the main information about each invoice.

| Column           | Data type     | Constraints           | Purpose                          |
| ---------------- | ------------- | --------------------- | -------------------------------- |
| `id`             | UUID          | Primary key           | Invoice identifier               |
| `business_id`    | UUID          | Foreign key, NOT NULL | Owning business                  |
| `customer_id`    | UUID          | Foreign key, NOT NULL | Customer being billed            |
| `invoice_number` | VARCHAR(50)   | NOT NULL              | Human-readable invoice reference |
| `status`         | VARCHAR(20)   | NOT NULL              | Draft, confirmed, or void        |
| `payment_status` | VARCHAR(20)   | NOT NULL              | Unpaid, partially paid, or paid  |
| `subtotal`       | NUMERIC(12,2) | NOT NULL              | Sum before adjustments           |
| `total`          | NUMERIC(12,2) | NOT NULL              | Final invoice amount             |
| `created_by`     | UUID          | Foreign key, NOT NULL | User who created it              |
| `confirmed_at`   | TIMESTAMPTZ   | NULL                  | Confirmation time                |
| `created_at`     | TIMESTAMPTZ   | NOT NULL              | Creation timestamp               |
| `updated_at`     | TIMESTAMPTZ   | NOT NULL              | Last update                      |

Invoice numbers must be unique within each business.

## 10. `invoice_items` table

An invoice can contain multiple products. This table stores each individual line item.

| Column         | Data type     | Constraints           | Purpose                      |
| -------------- | ------------- | --------------------- | ---------------------------- |
| `id`           | UUID          | Primary key           | Line item identifier         |
| `invoice_id`   | UUID          | Foreign key, NOT NULL | Associated invoice           |
| `product_id`   | UUID          | Foreign key, NOT NULL | Associated product           |
| `product_name` | VARCHAR(150)  | NOT NULL              | Product name at time of sale |
| `quantity`     | INTEGER       | NOT NULL, CHECK > 0   | Units purchased              |
| `unit_price`   | NUMERIC(12,2) | NOT NULL              | Price at time of sale        |
| `line_total`   | NUMERIC(12,2) | NOT NULL              | Quantity × unit price        |

Why store `product_name` and `unit_price` here when they already exist in `products`?

Because product details and prices can change. An invoice issued yesterday must retain yesterday's price even if the product price changes tomorrow.

## 11. `payments` table

Stores payments made against invoices.

| Column           | Data type     | Constraints           | Purpose                         |
| ---------------- | ------------- | --------------------- | ------------------------------- |
| `id`             | UUID          | Primary key           | Payment identifier              |
| `invoice_id`     | UUID          | Foreign key, NOT NULL | Invoice being paid              |
| `amount`         | NUMERIC(12,2) | NOT NULL, CHECK > 0   | Amount received                 |
| `payment_method` | VARCHAR(30)   | NOT NULL              | Cash, bank transfer, card, etc. |
| `reference`      | VARCHAR(100)  | NULL                  | Payment reference               |
| `recorded_by`    | UUID          | Foreign key, NOT NULL | User who recorded payment       |
| `created_at`     | TIMESTAMPTZ   | NOT NULL              | Payment timestamp               |

Each invoice can have multiple payment records.

For example:

- Invoice total: ₦30,000
- First payment: ₦10,000
- Second payment: ₦5,000
- Outstanding balance: ₦15,000
- Payment status: `partially_paid`

## 12. Complete database relationship overview

Core relationships

1:N means one-to-many; 1:1 means one-to-one.

Businesses

1:N

Users

Businesses

1:N

Products

Businesses

1:N

Customers

Products

1:1

Inventory

Products

1:N

Inventory Movements

Customers

1:N

Invoices

Invoices

1:N

Invoice Items

Products

1:N

Invoice Items

Invoices

1:N

Payments

### What we've designed

We now have nine core tables:

1. `businesses`
2. `users`
3. `products`
4. `inventory`
5. `inventory_movements`
6. `customers`
7. `invoices`
8. `invoice_items`
9. `payments`

We'll also add a refresh-token/session table when implementing authentication.
