from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    phone = Column(String(20), nullable=False)

    accounts = relationship("Account", back_populates="customer", cascade="all, delete-orphan")

class Account(Base):
    __tablename__ = "accounts"
    account_number = Column(String(20), primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    account_type = Column(String(20), nullable=False)  # savings / current
    balance = Column(Integer, nullable=False, default=0)

    customer = relationship("Customer", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account", cascade="all, delete-orphan")

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String(20), ForeignKey("accounts.account_number"), nullable=False)
    txn_type = Column(String(20), nullable=False)  # deposit / withdraw
    amount = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    account = relationship("Account", back_populates="transactions")
