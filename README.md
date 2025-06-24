# 🌙 Late Show API — Flask Code Challenge

A RESTful API for managing guests, episodes, and appearances on a fictional late-night TV show. Built with Flask, PostgreSQL, and JWT authentication.

---

## 🚀 Tech Stack

- **Flask** + Flask-SQLAlchemy
- **PostgreSQL**
- **Flask-Migrate** for database migrations
- **Flask-JWT-Extended** for token-based authentication
- **Postman** for API testing

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone git@github.com:Ali-Sheikh-Zubeir-Noor/late-show-api-challenge.git
cd late-show-api-challenge

2. Install Dependencies
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell

3. PostgreSQL Setup
Create your database:

sql
CREATE DATABASE late_show_db;
4. Environment Configuration
Update server/config.py with your PostgreSQL URI:

python
Copy code
SQLALCHEMY_DATABASE_URI = "postgresql://<username>:<password>@localhost:5432/late_show_db"

📦 How to Run

1. Run Migrations
export FLASK_APP=server.app
export PYTHONPATH=.
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

2. Seed the Database
python server/seed.py

3. Start the Server
flask run
🔐 Authentication Flow
Register: POST /register

Login: POST /login

Receive a JWT token and include it in protected routes using:

makefile
Authorization: Bearer <your_token>
📚 Routes Reference
Route	Method	Auth	Description
/register	POST	❌	Register a new user
/login	POST	❌	Login and get JWT
/guests	GET	❌	List all guests
/episodes	GET	❌	List all episodes
/episodes/<id>	GET	❌	Get episode and appearances
/episodes/<id>	DELETE	✅	Delete episode
/appearances	POST	✅	Create appearance

📬 Sample Requests
Register
http
Copy code
POST /register
Content-Type: application/json

{
  "username": "ali",
  "password": "123456"
}
Login
http
POST /login
Content-Type: application/json

{
  "username": "ali",
  "password": "123456"
}
Response:

json
{
  "access_token": "<your_token>"
}
Create Appearance (Protected)
http
POST /appearances
Authorization: Bearer <your_token>
Content-Type: application/json

{
  "rating": 5,
  "guest_id": 1,
  "episode_id": 2
}
📮 Postman Usage
Open Postman.

Import the file: challenge-4-lateshow.postman_collection.json

Use:

/register to sign up

/login to get your token

Add token to Authorization: Bearer <token> in protected requests

Test protected endpoints like POST /appearances and DELETE /episodes/<id>



