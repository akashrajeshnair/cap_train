from flask import Flask, jsonify, request

app = Flask(__name__)

accounts = []

@app.route('/accounts/<int:acc_no>', methods=['GET'])
def get_account(acc_no):
    try:
        for a in accounts:
            if a[0] == acc_no:
                account = a
        return jsonify({
            "account": account
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        print("GET account called")

@app.route('/accounts', methods=['POST'])
def create_account():
    try:
        data = request.get_json()
        acc_no = data.get('account_no')
        name = data.get('name')
        balance = data.get('balance')
        accounts.append(data)
        if not acc_no or not name or not balance:
            return jsonify({"error": "missing required fields"}), 400
        
        return jsonify({
            "message": "account created",
            "account": {
                "account_no": acc_no,
                "name": name,
                "balance": balance
            }
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        print("POST account called")

@app.route('/accounts/<int:acc_no>', methods=['PUT'])
def update_account(acc_no):
    try:
        updated_data = request.json
        for a in accounts:
            if a[0] == acc_no:
                a = updated_data
        return jsonify({
            "message": f"account {acc_no} updated",
            "updated_data": updated_data
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        print("PUT account called")

@app.route('/accounts/<int:acc_no>', methods=['DELETE'])
def delete_account(acc_no):
    try:
        for i, a in enumerate(accounts):
            if a[0] == acc_no:
                accounts.pop(i)
        return jsonify({"message": "deleted account"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        print("DELETE account called")

if __name__ == '__main__':
    app.run(port=3000, debug=True)