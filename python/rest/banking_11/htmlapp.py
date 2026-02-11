import flask
from flask import Flask

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
    if current_user is None:
        return flask.redirect('/login')
    return flask.render_template('index.html', username=user_data[current_user]['username'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    global current_user
    if flask.request.method == 'POST':
        for okey, idict in user_data.items():
            print(okey, idict['username'])
            if flask.request.form['username'] == idict["username"] and flask.request.form['password'] == idict["password"]:
                current_user = okey
                flask.flash('Logged in')
                return flask.redirect(flask.url_for('index'))    
        error = 'invalid credentials'
        return flask.render_template('login.html', error=error)
    return flask.render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if flask.request.method == 'POST':
        user = {
            "username": flask.request.form['username'],
            "password": flask.request.form['password']
        }
        account =  {
            "account_no": str(int(account_data[str(len(account_data)-1)]['account_no'])+ 1),
            "name": flask.request.form['name'],
            "balance": float(flask.request.form['balance']),
            "salary": float(flask.request.form['salary']),
            "aadhar_card_no": flask.request.form['aadhar_card_no'],
            "pan_card_no": flask.request.form['pan_card_no'],
            "phone_number": flask.request.form['phone_number'],
            "account_type": flask.request.form['account_type']
        }
        user_data[str(len(user_data))] = user
        account_data[str(len(account_data))] = account
        return flask.redirect('/login')
    return flask.render_template('register.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    global current_user
    if current_user is None:
        flask.flash("User isn't logged in... redirecting")
        return flask.redirect('/login')
    current_user = None
    return flask.redirect('/login')

@app.route('/loan')
def check_loan_eligibility():
    global current_user
    if account_data[current_user]['balance'] > 50000 or account_data[current_user]['salary'] > 30000:
        return flask.jsonify({"eligible": True})
    else:
        return flask.jsonify({"eligible": False})
    
@app.route('/profile', methods=['GET'])
def display_profile():
    return flask.render_template('profile.html', account = account_data[current_user])

@app.route('/profile/update', methods=['GET','POST'])
def update_profile():
    global current_user
    if flask.request.method == 'POST':
        data = {
            "account_no": flask.request.form['account_no'],
            "name": flask.request.form['name'],
            "balance": float(flask.request.form['balance']),
            "salary": float(flask.request.form['salary']),
            "aadhar_card_no": flask.request.form['aadhar_card_no'],
            "pan_card_no": flask.request.form['pan_card_no'],
            "phone_number": flask.request.form['phone_number'],
            "account_type": flask.request.form['account_type']
        }
        account_data[current_user] = data
        flask.flash('Account updated')
        return flask.redirect('/profile')
    return flask.render_template('profile_form.html', account = account_data[current_user])

@app.route('/profile/delete')
def delete_profile():
    global current_user
    user_data.pop(current_user)
    account_data.pop(current_user)
    print(account_data)
    return flask.redirect('/logout')

if __name__ == '__main__':
    app.run(port=3000, debug=True)