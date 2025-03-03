# FastAPI User Registration API



This is a simple FastAPI application that provides user registration with PostgreSQL.



## 🚀 Features

- Register users with hashed passwords

- PostgreSQL as the database

- FastAPI for building the API

- Uses `Base.metadata.create_all()` to create tables on startup



## 📌 Prerequisites

- Python 3.8+

- PostgreSQL installed and running

- `pip` and `virtualenv` installed

- Git installed



## ⚙️ Setup Guide



### 1️⃣ Clone the Repository  

### 2️⃣ Create a Virtual Environment and Install Dependencies  

```bash

python -m venv venv

source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

```



### 3️⃣ Set Up the PostgreSQL Database  

1. **Open PostgreSQL shell (`psql`)** and create the database:  

   ```sql

   CREATE DATABASE fastapi_users;

   CREATE USER myuser WITH PASSWORD 'mypassword';

   ALTER ROLE myuser SET client_encoding TO 'utf8';

   ALTER ROLE myuser SET timezone TO 'UTC';

   GRANT ALL PRIVILEGES ON DATABASE fastapi_users TO myuser;

   ```



2. **Update `DATABASE_URL` in `app/database.py`**  

   ```python

   DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/fastapi_users"

   ```



### 4️⃣ Run the FastAPI Server  

```bash

uvicorn main:app --reload

```

Server will start at **[http://127.0.0.1:8000](http://127.0.0.1:8000)**



### 5️⃣ Test the API  

- Open **Swagger UI** at **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

- Click **Try it out** on the `/users/register` endpoint

- Enter:

  ```json

  {

    "username": "john_doe",

    "email": "john@example.com",

    "password": "securepassword"

  }

  ```

- Click **Execute**

- Expected response:

  ```json

  {

    "message": "User registered successfully",

    "user_id": 1

  }

  ```



### 6️⃣ Database Verification  

Run the following SQL query in PostgreSQL to check if the user is registered:

```sql

SELECT * FROM users;

```



## 🛠 Tech Stack

- **FastAPI** 🚀

- **PostgreSQL** 🛢️

- **SQLAlchemy** ⚡
