from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from database import engine

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))

Base.metadata.create_all(bind=engine)
