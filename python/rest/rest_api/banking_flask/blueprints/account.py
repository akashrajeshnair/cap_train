from flask import Blueprint, request, jsonify
from models import Account, Base
from db import session_local, engine

account_bp = Blueprint('account', __name__, url_prefix='/accounts')

@account_bp.route('/', methods=['GET'])
def view_all_customers():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Authorization token required"}), 401
    with session_local() as session:
        accounts = session.query(Account).all()
        if accounts:
            return jsonify([{
                "account_no": a.account_no,
                "customer_id": a.customer_id,
                "account_type": a.account_type,
                "balance": a.balance
            } for a in accounts])
        return jsonify([])
        
@account_bp.route('/', methods=['POST'])
def create_customer():
    data = request.json
    customer_id = data.get('customer_id')
    account_type = data.get('account_type')
    balance = data.get('balance')
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Authorization token required"}), 401

    if not customer_id or not account_type or balance is None:
        return jsonify({"error": "missing fields"}), 400

    with session_local() as session:
        new_account = Account(customer_id=customer_id, account_type=account_type, balance=balance)
        session.add(new_account)
        session.commit()

        return jsonify({
            "message": "Account created",
            "account_id": new_account.account_no
        })
    
@account_bp.route('/<int:id>', methods=['GET'])
def view_one_customer(id):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Authorization token required"}), 401
    with session_local() as session:
        account = session.query(Account).filter_by(account_no=id).first()
        if account:
             return jsonify({
                "account_no": account.account_no,
                "customer_id": account.customer_id,
                "account_type": account.account_type,
                "balance": account.balance
            })
        return jsonify({"error": "Account not found"}), 404
    
@account_bp.route('/<int:id>', methods=['PUT'])
def update_customer(id):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Authorization token required"}), 401
    
    data = request.json
    
    with session_local() as session:
        account = session.query(Account).filter_by(account_no=id).first()

        if not account:
            return jsonify({"error": "Account does not exist"}), 404

        if 'customer_id' in data:
            account.customer_id = data.get('customer_id')
        if 'account_type' in data:
            account.account_type = data.get('account_type')
        if 'balance' in data:
            account.balance = data.get('balance')
        session.commit()

        return jsonify({
                "account_no": account.account_no,
                "customer_id": account.customer_id,
                "account_type": account.account_type,
                "balance": account.balance
            })

@account_bp.route('/<int:id>', methods=['DELETE'])
def delete_customer(id):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Authorization token required"}), 401
    
    with session_local() as session:
        account = session.query(Account).filter_by(account_no=id).first()
        
        if not account:
            return jsonify({"error": "account does not exist"}), 404
        
        session.delete(account)
        session.commit()
        return jsonify({"message": "account deleted"})