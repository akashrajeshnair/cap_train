from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(128), nullable=False)

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, index=True)
    salary = Column(Integer, nullable=False)
    annual_salary = Column(Integer, nullable=False)
    pf = Column(Integer, nullable=False)

