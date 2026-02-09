import flask
from flask import Flask, jsonify, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'

user_data = {
    "1": {
        "username": "admin",
        "password": "admin"
    },
    "2": {
        "username": "user",
        "password": "user"
    },
    "3": {
        "username": "akash",
        "password": "akash"
    },
    "4": {
        "username": "guest",
        "password": "guest"
    },
    "5": {
        "username": "bank",
        "password": "bank"
    }
}


current_user = None

account_data = {
    "1": {
        "account_no": "1001",
        "name": "admin",
        "balance": 10000.0,
        "salary": 40000.0,
        "aadhar_card_no": "1234-5678-9012",
        "pan_card_no": "ABCDE1234F",
        "phone_number": "9876543210",
        "account_type": "savings"
    },
    "2": {
        "account_no": "1002",
        "name": "user",
        "balance": 5000.0,
        "salary": 20000.0,
        "aadhar_card_no": "2345-6789-0123",
        "pan_card_no": "BCDEF2345G",
        "phone_number": "9876543211",
        "account_type": "fd"
    },
    "3": {
        "account_no": "1003",
        "name": "akash",
        "balance": 75000.0,
        "salary": 30000.0,
        "aadhar_card_no": "3456-7890-1234",
        "pan_card_no": "CDEFG3456H",
        "phone_number": "9876543212",
        "account_type": "savings"
    },
    "4": {
        "account_no": "1004",
        "name": "guest",
        "balance": 2000.0,
        "salary": 5000.0,
        "aadhar_card_no": "4567-8901-2345",
        "pan_card_no": "DEFGH4567I",
        "phone_number": "9876543213",
        "account_type": "savings"
    },
    "5": {
        "account_no": "1005",
        "name": "bank",
        "balance": 100000.0,
        "salary": 10000.0,
        "aadhar_card_no": "5678-9012-3456",
        "pan_card_no": "EFGHI5678J",
        "phone_number": "9876543214",
        "account_type": "recurring"
    }
}

@app.route('/')
def index():
    global current_user
    if current_user is None:
        return jsonify({"error": "Not logged in"}), 401
    return jsonify({
        "message": "Welcome",
        "username": user_data[current_user]['username']
    })

@app.route('/login', methods=['POST'])
def login():
    global current_user
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    username = data.get('username')
    password = data.get('password')
    
    for okey, idict in user_data.items():
        if username == idict["username"] and password == idict["password"]:
            current_user = okey
            return jsonify({
                "message": "Logged in successfully",
                "user_id": current_user,
                "username": username
            })
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    user = {
        "username": data.get('username'),
        "password": data.get('password')
    }
    
    new_id = str(len(user_data) + 1)
    new_account_no = str(int(account_data[str(len(account_data))]['account_no']) + 1)
    
    account = {
        "account_no": new_account_no,
        "name": data.get('name'),
        "balance": float(data.get('balance', 0)),
        "salary": float(data.get('salary', 0)),
        "aadhar_card_no": data.get('aadhar_card_no'),
        "pan_card_no": data.get('pan_card_no'),
        "phone_number": data.get('phone_number'),
        "account_type": data.get('account_type', 'savings')
    }
    
    user_data[new_id] = user
    account_data[new_id] = account
    
    return jsonify({
        "message": "User registered successfully",
        "user_id": new_id,
        "account_no": new_account_no
    }), 201

@app.route('/logout', methods=['POST'])
def logout():
    global current_user
    if current_user is None:
        return jsonify({"error": "User isn't logged in"}), 401
    current_user = None
    return jsonify({"message": "Logged out successfully"})

@app.route('/loan')
def check_loan_eligibility():
    global current_user
    if current_user is None:
        return jsonify({"error": "Not logged in"}), 401
    
    balance = account_data[current_user]['balance']
    salary = account_data[current_user]['salary']
    eligible = balance > 50000 or salary > 30000
    
    return jsonify({
        "eligible": eligible,
        "balance": balance,
        "salary": salary
    })

@app.route('/profile', methods=['GET'])
def display_profile():
    global current_user
    if current_user is None:
        return jsonify({"error": "Not logged in"}), 401
    
    return jsonify({
        "user": user_data[current_user],
        "account": account_data[current_user]
    })

@app.route('/profile/update', methods=['PUT', 'POST'])
def update_profile():
    global current_user
    if current_user is None:
        return jsonify({"error": "Not logged in"}), 401
    
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    account_data[current_user].update({
        "name": data.get('name', account_data[current_user]['name']),
        "balance": float(data.get('balance', account_data[current_user]['balance'])),
        "salary": float(data.get('salary', account_data[current_user]['salary'])),
        "aadhar_card_no": data.get('aadhar_card_no', account_data[current_user]['aadhar_card_no']),
        "pan_card_no": data.get('pan_card_no', account_data[current_user]['pan_card_no']),
        "phone_number": data.get('phone_number', account_data[current_user]['phone_number']),
        "account_type": data.get('account_type', account_data[current_user]['account_type'])
    })
    
    return jsonify({
        "message": "Profile updated successfully",
        "account": account_data[current_user]
    })

@app.route('/profile/delete', methods=['DELETE'])
def delete_profile():
    global current_user
    if current_user is None:
        return jsonify({"error": "Not logged in"}), 401
    
    deleted_user = user_data.pop(current_user)
    deleted_account = account_data.pop(current_user)
    current_user = None
    
    return jsonify({
        "message": "Profile deleted successfully",
        "deleted_user": deleted_user['username'],
        "deleted_account_no": deleted_account['account_no']
    })

if __name__ == '__main__':
    app.run(port=3000, debug=True)