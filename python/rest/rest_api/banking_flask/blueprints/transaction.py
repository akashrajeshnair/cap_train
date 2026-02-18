from flask import Blueprint, request, jsonify
from db import session_local
from models import Transaction, Account
from datetime import datetime

transaction_bp = Blueprint('transactions', __name__)

@transaction_bp.route('/accounts/<int:account_no>/transactions', methods=['GET'])
def get_transactions(account_no):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Authorization token required"}), 401
    
    with session_local() as session:
        account = session.query(Account).filter_by(account_no=account_no).first()
        if not account:
            return jsonify({"error": "Account not found"}), 404
        
        transactions = session.query(Transaction).filter_by(account_no=account_no).all()
        return jsonify([{
            'id': t.id,
            'account_no': t.account_no,
            'transaction_type': t.transaction_type,
            'amount': t.amount,
            'date': t.date.isoformat() if t.date else None
        } for t in transactions]), 200

@transaction_bp.route('/accounts/<int:account_no>/withdraw', methods=['POST'])
def withdraw(account_no):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Authorization token required"}), 401
    data = request.json
    
    if not data or not data.get('amount'):
        return jsonify({"error": "Amount is required"}), 400
    
    amount = data['amount']
    
    if amount <= 0:
        return jsonify({"error": "Amount must be greater than 0"}), 400
    
    with session_local() as session:
        account = session.query(Account).filter_by(account_no=account_no).first()
        
        if not account:
            return jsonify({"error": "Account not found"}), 404
        
        if account.balance < amount:
            return jsonify({
                "error": "Insufficient balance",
                "available_balance": account.balance
            }), 400
        
        account.balance -= amount
    
        transaction = Transaction(
            account_no=account_no,
            transaction_type='withdraw',
            amount=amount,
            date=datetime.utcnow()
        )
        session.add(transaction)
        session.commit()
        
        return jsonify({
            'message': 'Withdrawal succeeded',
            'transaction': {
                'id': transaction.id,
                'account_no': transaction.account_no,
                'transaction_type': transaction.transaction_type,
                'amount': transaction.amount,
                'date': transaction.date.isoformat()
            },
            'new_balance': account.balance
        }), 200

@transaction_bp.route('/accounts/<int:account_no>/deposit', methods=['POST'])
def deposit(account_no):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Authorization token required"}), 401
    
    data = request.json
    
    if not data or not data.get('amount'):
        return jsonify({"error": "Amount is required"}), 400
    
    amount = data['amount']
    
    if amount <= 0:
        return jsonify({"error": "Amount must be greater than 0"}), 400
    
    with session_local() as session:
        account = session.query(Account).filter_by(account_no=account_no).first()
        
        if not account:
            return jsonify({"error": "Account not found"}), 404
        
        account.balance += amount

        transaction = Transaction(
            account_no=account_no,
            transaction_type='deposit',
            amount=amount,
            date=datetime.utcnow()
        )
        session.add(transaction)
        session.commit()
        
        return jsonify({
            'message': 'Deposit successful',
            'transaction': {
                'id': transaction.id,
                'account_no': transaction.account_no,
                'transaction_type': transaction.transaction_type,
                'amount': transaction.amount,
                'date': transaction.date.isoformat()
            },
            'new_balance': account.balance
        }), 200



    

