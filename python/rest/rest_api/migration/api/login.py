from flask import Blueprint, request, jsonify
from db.models import User, Base
from db.database import session_local, engine
import jwt
import datetime
import bcrypt

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
SECRET_KEY = 'hello'
s = bcrypt.gensalt()
user_id = None

Base.metadata.create_all(bind=engine)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "username and password required"}), 400
    
    auth_header = request.headers.get('Authorization')

    with session_local() as session:
        user_count = session.query(User).count()

        if user_count > 0:
            if not auth_header or not auth_header.startswith('Bearer '):
                return jsonify({"error": "Authorization token required"}), 401
            
            token = auth_header.split()[1]
            try:
                jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            except:
                return jsonify({"error": "invalid token"}), 401
            
        existing_user = session.query(User).filter_by(username=username).first()
        if existing_user:
            return jsonify({"error": "user already exists"}), 400
        
        b_password = password.encode()
        hashed_password = bcrypt.hashpw(b_password, s)
        
        new_user = User(username=username, password=hashed_password)
        session.add(new_user)
        session.commit()

        return jsonify({
            "message": f"User {username} created successfully",
            "user_id": new_user.id
        })
    
@auth_bp.route('/login', methods=['POST'])
def login():
    global user_id
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "username and password required"}), 400
    
    with session_local() as session:
        user = session.query(User).filter_by(username=username).first()
        b_password = password.encode()
        db_password = user.password
        b_db_password = db_password.encode()
        if not user:
            return jsonify({"error": "user not found"}), 404
        if not bcrypt.checkpw(b_password, b_db_password):
            return jsonify({"error": "wrong password"}), 401
        
        payload = {
            "user_id": user.id,
            "username": user.username,
            "exp": datetime.datetime.now() + datetime.timedelta(hours=1)
        }

        user_id = user.id
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({
            "message": f"Welcome {username}",
            "user_id": user.id,
            "token": token
        })