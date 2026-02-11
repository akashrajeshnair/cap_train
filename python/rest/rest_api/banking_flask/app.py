from flask import Flask
from banking_flask.models import Base
from banking_flask.db import engine
from banking_flask.blueprints.customer import customer_bp
from banking_flask.blueprints.account import account_bp
from banking_flask.blueprints.transaction import transaction_bp

Base.metadata.create_all(engine)
app = Flask(__name__)

app.register_blueprint(customer_bp)
app.register_blueprint(account_bp)
app.register_blueprint(transaction_bp)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
