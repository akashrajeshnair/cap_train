from flask import Flask, jsonify, request

app = Flask(__name__)

users = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"message": "Returning list of users", "users": users})

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    users.append(new_user)
    return jsonify({
        "message": "User created",
        "user": new_user
    })

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    updated_user = request.json
    users[id-1] = updated_user
    return jsonify({
        "message": "updated user",
        "updated_user": updated_user
    })

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    users.pop(id-1)
    return jsonify({
        "message": f"user with id: {id} deleted"
    })

if __name__ == '__main__':
    app.run(port=3000, debug=True)