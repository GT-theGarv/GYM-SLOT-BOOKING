from pathlib import Path

from sqlalchemy import func, select, text
from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from dtos import UserDTO,createUserDTO,bookingDTO
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
import random

app = FastAPI()
FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/Frontend", StaticFiles(directory=FRONTEND_DIR), name="Frontend")

from SQL import Base, engine
from SQL import Member, SixAM, SevenAM, EightAM
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    print("Gym database tables are ready!")
    yield
@app.get("/")
def root():
    return RedirectResponse(url="/Frontend/signin.html")

@app.post("/")
def signin(User: UserDTO):
    global email, password
    from sqlalchemy import text
    with engine.connect() as connection:
        user = connection.execute(
            text("SELECT * FROM members WHERE email = :email AND password = :password"),
            {"email": User.email, "password": User.password},
            ).fetchone()
    if user:
        email= User.email
        password = User.password
        return 0
    else:
        return 1
@app.post("/signup")
def signup(User: createUserDTO):
    with engine.begin() as connection:
        existing_user = connection.execute(
            text("SELECT * FROM members WHERE email = :email"),
            {"email": User.email},
        ).fetchone()
        if existing_user:
            return 1
        else:
            connection.execute(
                text("INSERT INTO members (name, email, password) VALUES (:name, :email, :password)"),
                {"name": User.name, "email": User.email, "password": User.password},
            )
            return 0

@app.post("/logout")
def logout():
    global email,password
    email=""
    password=""
    return 0

@app.post("/book")
def book(ID: bookingDTO):
    slot=ID.ID+"am"
    with engine.begin() as connection:
        count = connection.scalar(select(func.count()).select_from(slot))
        if count<10:
            otp=random.random()
            connection.execute(text("INSERT INTO members (email, otp) VALUES (:email, :otp)"),
            {"email":email, "otp": otp},)
            count+=1
            return {"otp":otp,"count":count}
        else:
            return 10
    return {"message": "Booking request received"}