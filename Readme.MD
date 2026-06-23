# 🛒 Ecommerce Repo — Products & Orders

A small, focused Django + Django REST Framework project built to **learn and practice real backend engineering concepts** — not to be a full-blown ecommerce platform.

> **Scope on purpose:** This project only ever deals with two things — **Products** and **Orders**. Every concept below (serializers, admin, inheritance, N+1, cardinalities) will be learned and applied *inside* this small scope, so the focus stays on depth over breadth.

---

## 📌 Project Status

| | |
|---|---|
| **Framework** | Django 6.0.6 |
| **API Layer** | Django REST Framework |
| **Database** | SQLite (dev) |
| **Apps so far** | `products` |
| **Apps planned** | `orders` |
| **Stage** | 🟡 Foundations — models & constraints in place, API layer not yet built |

---

## ✅ What's Done So Far

```
ecommerce/
├── ecommerce/              # Project config (settings, urls, wsgi, asgi)
└── products/                # First app — catalog domain
    ├── models.py             # Category, Product
    ├── admin.py               # empty — not registered yet
    ├── views.py                # placeholder view only
    ├── urls.py                  # /api/greet/ only
    └── migrations/0001_initial.py
```

### 1. Project bootstrapped
- Django project `ecommerce` created and configured.
- `rest_framework` added to `INSTALLED_APPS` — DRF is wired in, ready to be used.
- SQLite configured as the dev database.

### 2. `products` app — domain modeling

#### `Category`

| Field | Type | Notes |
|---|---|---|
| `name` | `CharField` | Primary key. No separate `id` field. |

#### `Product`

| Field | Type | Notes |
|---|---|---|
| `category` | `ForeignKey → Category` | `on_delete=PROTECT` |
| `name` | `CharField` | Product name |
| `description` | `TextField` | Maximum 800 characters |
| `price` | `DecimalField` | Must be greater than `0` at the database level |
| `quantity` | `PositiveIntegerField` | Must be greater than or equal to `0` at the database level |
| `created_at` | `DateTimeField` | Auto-managed timestamp |
| `updated_at` | `DateTimeField` | Auto-managed timestamp |



---

## 🧭 What's Coming Next (Roadmap)

These are the concepts being deliberately learned, in this exact small project, one at a time:

### 1. Serializers (DRF)
- Build `ProductSerializer` and `CategorySerializer`.
- Learn `ModelSerializer` vs plain `Serializer`.
- Add field-level and object-level **validation**.
- Connect serializers to real views (replacing the placeholder `greet_user`).

### 2. Admin
- Register `Category` and `Product` in `admin.py`.
- Customize `list_display`, `search_fields`, `list_filter`.
- Use the admin to *see* the effect of constraints and relationships hands-on.

### 3. Inheritance (Multi-Table Inheritance)
- Introduce the `orders` app.
- Likely shape: an abstract/base `Order` concept, exploring **Multi-Table Inheritance (MTI)** vs abstract base classes vs proxy models — and how each behaves in queries and migrations.

### 4. Cardinalities
- Model the real relationship between **Orders and Products**:
  - One Order → many Products (likely via a through-model like `OrderItem`, since price/quantity at time of order matters).
  - Revisit `Category ↔ Product` (one-to-many) as the baseline example.
- Understand one-to-one, one-to-many, and many-to-many in practice — not just in theory.

### 5. N+1 Query Problem
- Deliberately *cause* an N+1 problem (e.g. looping over orders and accessing `order.product.name`).
- Fix it using `select_related` (for FK/one-to-one) and `prefetch_related` (for reverse FK/many-to-many).
- Measure the difference using Django's query count / debug tools.

### 6. General software quality upgrades
- Replace placeholder views with proper `APIView` / `ViewSet` based endpoints.
- Add meaningful tests in `tests.py` for models and API behavior.
- Add a `.gitignore` (currently missing) to keep `.venv/`, `__pycache__/`, and `db.sqlite3` out of version control.
- Move the `SECRET_KEY` out of source and into an environment variable before this ever goes near production.

---

## 🗺️ Target Domain Model (where this is heading)

```
Category 1 ──── * Product
                    │
                    │ *
                    │
                 OrderItem
                    │
                    │ *
                    │
                  Order 1
```

Just **two real-world entities — Products and Orders** — but enough relationship depth to genuinely practice serializers, admin, inheritance, cardinalities, and query optimization.

---

## 🚀 Running the Project

```bash
# from the ecommerce/ directory
python manage.py migrate
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/api/greet/`

---

## 🧱 Tech Stack

- **Backend:** Django 6.0.6
- **API:** Django REST Framework
- **Database:** SQLite (development)
- **Language:** Python

---

*This README is a living document — it will be updated as serializers, admin, inheritance, cardinalities, and N+1 fixes are implemented in the `orders` and `products` apps.*