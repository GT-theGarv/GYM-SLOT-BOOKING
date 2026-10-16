# The Gym

A small gym-slot booking app with a static HTML/CSS/JavaScript frontend, a FastAPI backend, and a PostgreSQL database. Users can create an account, sign in, and request a booking for one of the listed morning sessions.

## Project layout

```text
backend/
  SQL.py             Database connection and SQLAlchemy models
  dtos.py            Request data models
  logincheck.py      FastAPI routes and static frontend hosting
frontend/
  signin.html        Sign-in page
  signup.html        Account registration page
  main.html          Session listing and booking page
  logincheck.js      Frontend sign-in, sign-up, and booking requests
  *.css              Page styles
```

## Requirements

- Python 3.9 or newer
- PostgreSQL

Install the Python dependencies:

```powershell
py -m pip install -r requirements.txt
```

## Configure the database

Create a `.env` file in the project root with PostgreSQL connection details:

```dotenv
USER=your_postgres_user
PASSWORD=your_postgres_password
HOST=localhost
PORT=5432
DATABASE=gym
```

Keep real credentials out of source control. The backend creates the configured database if it does not exist, then creates its tables. The PostgreSQL account must have permission to create databases and tables.

## Run locally

From the project root, start the API server:

```powershell
cd backend
py -m uvicorn logincheck:app --reload
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to be redirected to the sign-in page. The frontend is served by FastAPI under `/Frontend`.

## API overview

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/` | Redirect to the sign-in page |
| `POST` | `/` | Sign in with an email and password |
| `POST` | `/signup` | Register a member |
| `POST` | `/logout` | Clear the current in-memory login values |
| `POST` | `/book` | Request a booking |

The frontend is served at `/Frontend`; these routes are intended to be called by the app rather than used as standalone API documentation.
