from flask import Flask
from flask_smorest import Api, Blueprint, abort
from sqlalchemy.exc import IntegrityError
from db import SessionLocal, engine
from models import Base, Customer, Account, Transaction
from schemas import CustomerCreateSchema, CustomerSchema, AccountCreateSchema, AccountSchema, TransactionCreateSchema, TransactionSchema

app = Flask(__name__)
app.config["API_TITLE"] = "Bank Account Management"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

Base.metadata.create_all(bind=engine)

customer_bp = Blueprint("customers", "customers", url_prefix="/customers")
account_bp = Blueprint("accounts", "accounts", url_prefix="/accounts")

@customer_bp.route("", methods=["POST"])
@customer_bp.arguments(CustomerCreateSchema)
@customer_bp.response(201, CustomerSchema)
def create_customer(payload):
    with SessionLocal() as session:
        customer = Customer(**payload)
        session.add(customer)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
            abort(400, message="Email already exists")
        session.refresh(customer)
        return customer

@customer_bp.route("/<int:customer_id>", methods=["GET"])
@customer_bp.response(200, CustomerSchema)
def get_customer(customer_id):
    with SessionLocal() as session:
        customer = session.query(Customer).filter(Customer.id == customer_id).first()
        if not customer:
            abort(404, message="Customer not found")
        return customer

@account_bp.route("", methods=["POST"])
@account_bp.arguments(AccountCreateSchema)
@account_bp.response(201, AccountSchema)
def create_account(payload):
    with SessionLocal() as session:
        customer = session.query(Customer).filter(Customer.id == payload["customer_id"]).first()
        if not customer:
            abort(404, message="Customer not found")
        account = Account(**payload)
        session.add(account)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
            abort(400, message="Account number already exists")
        session.refresh(account)
        return account

@account_bp.route("/<string:account_number>", methods=["GET"])
@account_bp.response(200, AccountSchema)
def get_account(account_number):
    with SessionLocal() as session:
        account = session.query(Account).filter(Account.account_number == account_number).first()
        if not account:
            abort(404, message="Account not found")
        return account

@account_bp.route("/<string:account_number>/deposit", methods=["POST"])
@account_bp.arguments(TransactionCreateSchema)
@account_bp.response(200, AccountSchema)
def deposit(payload, account_number):
    with SessionLocal() as session:
        account = session.query(Account).filter(Account.account_number == account_number).first()
        if not account:
            abort(404, message="Account not found")
        amount = payload["amount"]
        if amount <= 0:
            abort(400, message="Amount must be positive")
        account.balance += amount
        txn = Transaction(account_number=account_number, txn_type="deposit", amount=amount)
        session.add(txn)
        session.commit()
        session.refresh(account)
        return account

@account_bp.route("/<string:account_number>/withdraw", methods=["POST"])
@account_bp.arguments(TransactionCreateSchema)
@account_bp.response(200, AccountSchema)
def withdraw(payload, account_number):
    with SessionLocal() as session:
        account = session.query(Account).filter(Account.account_number == account_number).first()
        if not account:
            abort(404, message="Account not found")
        amount = payload["amount"]
        if amount <= 0:
            abort(400, message="Amount must be positive")
        if account.balance < amount:
            abort(400, message="Insufficient balance")
        account.balance -= amount
        txn = Transaction(account_number=account_number, txn_type="withdraw", amount=amount)
        session.add(txn)
        session.commit()
        session.refresh(account)
        return account

@account_bp.route("/<string:account_number>/transactions", methods=["GET"])
@account_bp.response(200, TransactionSchema(many=True))
def get_transactions(account_number):
    with SessionLocal() as session:
        account = session.query(Account).filter(Account.account_number == account_number).first()
        if not account:
            abort(404, message="Account not found")
        txns = session.query(Transaction).filter(Transaction.account_number == account_number).order_by(Transaction.id.desc()).all()
        return txns

api.register_blueprint(customer_bp)
api.register_blueprint(account_bp)

if __name__ == "__main__":
    app.run(debug=True)
