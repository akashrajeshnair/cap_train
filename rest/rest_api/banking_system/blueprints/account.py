from flask_smorest import Blueprint
from flask.views import MethodView
from banking_system.schema import AccountSchema

account_blp = Blueprint(
    'accounts',
    __name__,
    description = "Account CRUD Operations"
)

accounts = []

@account_blp.route('/accounts')
class AccountList(MethodView):
    @account_blp.response(200, AccountSchema(many=True))
    def get(self):
        """Get all accounts"""
        return accounts
    
    @account_blp.arguments(AccountSchema)
    @account_blp.response(201, AccountSchema)
    def post(self, account_data):
        """Create a new account"""
        account_data['account_no'] = len(accounts) + 1
        accounts.append(account_data)
        return account_data

@account_blp.route('/accounts/<int:id>') 
class Account(MethodView):
    @account_blp.response(200, AccountSchema)
    def get(self, id):
        """Get an account by account number"""
        for a in accounts:
            if a["account_no"] == id:
                return a
        return {"message": "Account not found"}, 404
    
    @account_blp.arguments(AccountSchema)
    @account_blp.response(201, AccountSchema)
    def put(self, account_data, id):
        """Update a account"""
        for a in accounts:
            if a["account_no"] == id:
                a.update(account_data)
        return account_data
    
    def delete(self, id):
        """Delete an account"""
        global accounts
        for a in accounts:
            if a["account_no"] == id:
                accounts = [acc for acc in accounts if acc["account_no"] != id]
                return {"message": "Account deleted successfully"}, 200
        return {"message": "Account not found"}, 404

    

