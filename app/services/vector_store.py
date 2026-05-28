from sqlalchemy import create_engine, text
from pgvector.sqlalchemy import Vector
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)


def initialize_db():

    with engine.connect() as conn:

        conn.execute(text(
            "CREATE EXTENSION IF NOT EXISTS vector"
        ))

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS incidents (
            id SERIAL PRIMARY KEY,
            incident TEXT,
            diagnosis TEXT,
            fix TEXT
        )
        """))

        conn.commit()