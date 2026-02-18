from flask import Blueprint, request, jsonify
from models import Customer, Base
from db import session_local, engine
import jwt
import bcrypt
import datetime

SECRET_KEY = 'hello'
s = bcrypt.gensalt()
customer_bp = Blueprint('customer', __name__, url_prefix='/customers')

@customer_bp.route('/', methods=['GET'])
def view_all_customers():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Authorization token required"}), 401
    with session_local() as session:
        customers = session.query(Customer).all()
        if customers:
            return jsonify([{
                "id": c.id,
                "name": c.name,
                "email": c.email,
                "phone_number": c.phone_number
            } for c in customers])
        return jsonify([])
        
@customer_bp.route('/', methods=['POST'])
def create_customer():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    phone_number = data.get('phone_number')
    print(name, email, phone_number)

    if not name or not email or not phone_number:
        return jsonify({"error": "missing fields"}), 400

    with session_local() as session:
        new_customer = Customer(name=name, email=email, phone_number=phone_number)
        session.add(new_customer)
        session.commit()

        payload = {
            "name": new_customer.name,
            "exp": datetime.datetime.now() + datetime.timedelta(hours=1)
        }

        customer_id = new_customer.id
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({
            "message": f"Welcome {new_customer.name}",
            "customer_id": new_customer.id,
            "token": token
        })
    
@customer_bp.route('/<int:id>', methods=['GET'])
def view_one_customer(id):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Authorization token required"}), 401
    with session_local() as session:
        customer = session.query(Customer).filter_by(id=id).first()
        if customer:
             return jsonify({
                "id": customer.id,
                "name": customer.name,
                "email": customer.email,
                "phone_number": customer.phone_number
            })
        return jsonify({"error": "Customer not found"}), 404
    
@customer_bp.route('/<int:id>', methods=['PUT'])
def update_customer(id):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Authorization token required"}), 401
    
    data = request.json

    with session_local() as session:
        customer = session.query(Customer).filter_by(id=id).first()

        if not customer:
            return jsonify({"error": "Customer does not exist"}), 404

        if 'name' in data:
            customer.name = data.get('name')
        if 'email' in data:
            customer.email = data.get('email')
        if 'phone_number' in data:
            customer.phone_number = data.get('phone_number')

        session.commit()

        return jsonify({
                "id": customer.id,
                "name": customer.name,
                "email": customer.email,
                "phone_number": customer.phone_number
            })

@customer_bp.route('/<int:id>', methods=['DELETE'])
def delete_customer(id):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Authorization token required"}), 401

    with session_local() as session:
        customer = session.query(Customer).filter_by(id=id).first()
        
        if not customer:
            return jsonify({"error": "customer does not exist"}), 404
        
        session.delete(customer)
        session.commit()
        return jsonify({"message": "customer deleted"})