
# 🎬 Late Show API — Flask REST Code Challenge

This is a RESTful API for managing a Late Night Show system. It uses Flask, PostgreSQL, SQLAlchemy, and JWT for token-based authentication.

---

## 📦 Technologies Used

- Flask
- PostgreSQL
- SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- Postman
- Python 3.12+

---

## 🛠 Setup Instructions

### 🔧 1. Clone the Repo

```bash
git clone https://github.com/<your-username>/late-show-api-challenge.git
cd late-show-api-challenge
```

### 🐍 2. Create Virtual Environment and Install Dependencies

```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
```

### 🐘 3. PostgreSQL Setup

Log into Postgres:

```bash
sudo -i -u postgres
psql
```

Then run:

```sql
CREATE USER myuser WITH PASSWORD 'mypassword';
CREATE DATABASE late_show_db;
GRANT ALL PRIVILEGES ON DATABASE late_show_db TO myuser;
\q
```

### 🧪 4. Update Your DB Config

In `server/config.py`, set:

```python
SQLALCHEMY_DATABASE_URI = "postgresql://myuser:mypassword@localhost:5432/late_show_db"
```

---

## ▶️ How to Run

```bash
export FLASK_APP=server.app:create_app

# Initialize DB (only once)
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Seed data
python -m server.seed

# Start the server
flask run
```

---

## 🔐 Auth Flow

### 🔸 Register

**POST** `/register`

```json
{
  "username": "admin",
  "password": "1234"
}
```

---

### 🔸 Login

**POST** `/login`

```json
{
  "username": "admin",
  "password": "1234"
}
```

**Returns:**

```json
{
  "token": "your_jwt_token"
}
```

---

### 🔸 Using the Token

For protected routes, set a header:

```
Authorization: Bearer your_jwt_token
```

---

## 🌐 API Routes + Sample Requests

| Method | Route                       | Auth? | Description                         |
|--------|-----------------------------|-------|-------------------------------------|
| POST   | `/register`                 | ❌    | Create a new user                   |
| POST   | `/login`                    | ❌    | Login and get token                 |
| GET    | `/episodes`                 | ❌    | List all episodes                   |
| GET    | `/episodes/<id>`           | ❌    | Get episode with guest appearances  |
| DELETE | `/episodes/<id>`           | ✅    | Delete episode + its appearances    |
| GET    | `/guests`                   | ❌    | List all guests                     |
| POST   | `/appearances`             | ✅    | Create guest appearance             |

---

### 🔁 Example: `POST /appearances`

**Request:**

```json
{
  "guest_id": 1,
  "episode_id": 2,
  "rating": 5
}
```

**Header:**

```
Authorization: Bearer your_jwt_token
```

**Response:**

```json
{
  "id": 4,
  "rating": 5,
  "guest_id": 1,
  "episode_id": 2
}
```

---

## 📮 Postman Usage Guide

### ✅ Step 1: Import Collection

1. Download: [`challenge-4-lateshow.postman_collection.json`](./challenge-4-lateshow.postman_collection.json)
2. Open Postman → Import → Upload the file

### ✅ Step 2: Run Requests

- Test `/register` and `/login`
- Copy the returned token
- Add it to `Authorization` → `Bearer Token` tab
- Test protected routes like `/appearances` and `DELETE /episodes/:id`

---

## 🔗 GitHub Repository

https://github.com/Ali-Sheikh-Zubeir-Noor/late-show-api-challenge
---

## ✅ Submission Checklist

- [x] PostgreSQL used
- [x] MVC file structure
- [x] Models and relationships defined
- [x] JWT authentication implemented
- [x] Protected routes secured
- [x] Working migrations and seed data
- [x] Postman tested
- [x] Complete README