from flask_smorest import Blueprint, abort
from flask.views import MethodView
from banking_system.schema import TransactionSchema
from banking_system.blueprints.account import accounts
from marshmallow import Schema, fields
from datetime import datetime

transaction_blp = Blueprint(
    'transaction',
    __name__,
    description = "Transaction CRUD Operations"
)

transactions = []

class AmountSchema(Schema):
    amount = fields.Int(required=True)

@transaction_blp.route('/accounts/<int:account_no>/transactions') 
class TransactionList(MethodView):
    @transaction_blp.response(200, TransactionSchema(many=True))
    def get(self, account_no):
        """Get all transactions for an account"""
        account_transactions = []
        for t in transactions:
            if t["account_no"] == account_no:
                account_transactions.append(t)
        return account_transactions

@transaction_blp.route('/accounts/<int:account_no>/withdraw')
class Withdraw(MethodView):
    @transaction_blp.arguments(AmountSchema)
    @transaction_blp.response(200, TransactionSchema)
    def post(self, amount_data, account_no):
        """Withdraw money from account"""
        amount = amount_data['amount']
        
        account = None
        for acc in accounts:
            if acc["account_no"] == account_no:
                account = acc
                break
        
        if not account:
            abort(404, message="Account not found")
        if amount <= 0:
            abort(400, message="Amount must be greater than 0")
        if account["balance"] < amount:
            abort(400, message=f"Insufficient balance. Available balance: {account['balance']}")

        account["balance"] -= amount
        transaction = {
            "id": len(transactions) + 1,
            "account_no": account_no,
            "transaction_type": "withdraw",
            "amount": amount,
            "date": datetime.now()
        }
        transactions.append(transaction)
        
        return transaction

@transaction_blp.route('/accounts/<int:account_no>/deposit')
class Deposit(MethodView):
    @transaction_blp.arguments(AmountSchema)
    @transaction_blp.response(200, TransactionSchema)
    def post(self, amount_data, account_no):
        """Deposit money to account"""
        amount = amount_data['amount']
        
        account = None
        for acc in accounts:
            if acc["account_no"] == account_no:
                account = acc
                break
        
        if not account:
            abort(404, message="Account not found")
        if amount <= 0:
            abort(400, message="Amount must be greater than 0")
        
        account["balance"] += amount

        transaction = {
            "id": len(transactions) + 1,
            "account_no": account_no,
            "transaction_type": "deposit",
            "amount": amount,
            "date": datetime.now()
        }
        transactions.append(transaction)
        
        return transaction



    

