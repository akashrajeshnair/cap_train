from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Update if needed: mysql+pymysql://user:password@host:port/dbname
DATABASE_NAME = "bankdb"
ROOT_URL = "mysql+pymysql://root:root@localhost:3306"

engine = create_engine(ROOT_URL, echo=True)

with engine.connect() as connection:
    connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"))

DATABASE_URL = f"{ROOT_URL}/{DATABASE_NAME}"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
