from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=False)
    

class Account(Base):
    __tablename__ = 'accounts'
    
    account_no = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, nullable=False)
    account_type = Column(String(50), nullable=False)
    balance = Column(Integer, default=0, nullable=False)
    
class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    account_no = Column(Integer, nullable=False)
    transaction_type = Column(String(50), nullable=False)
    amount = Column(Integer, nullable=False)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)