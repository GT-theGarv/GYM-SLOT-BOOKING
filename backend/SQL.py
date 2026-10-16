
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import database_exists, create_database

from dotenv import load_dotenv
import os
load_dotenv()
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DATABASE = os.getenv("DATABASE")

ADMIN_URL = (
    f"postgresql+psycopg2://{USER}:{PASSWORD}"
    f"@{HOST}:{PORT}/postgres"
)
admin_engine = create_engine(ADMIN_URL)
if not database_exists(
    f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
):
    create_database(
        f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    )

DATABASE_URL = (
    f"postgresql+psycopg2://{USER}:{PASSWORD}"
    f"@{HOST}:{PORT}/{DATABASE}"
)

engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Member(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)


class SixAM(Base):
    __tablename__ = "6am"
    email = Column(String(255), primary_key=True)
    otp = Column(String(10), nullable=False)

class SevenAM(Base):
    __tablename__ = "7am"
    email = Column(String(255), primary_key=True)
    otp = Column(String(10), nullable=False)

class EightAM(Base):
    __tablename__ = "8am"
    email = Column(String(255), primary_key=True)
    otp = Column(String(10), nullable=False)

Base.metadata.create_all(bind=engine)
