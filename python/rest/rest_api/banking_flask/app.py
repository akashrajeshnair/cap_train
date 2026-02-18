from flask import Flask
from flask_cors import CORS
from models import Base
from db import engine
from blueprints.customer import customer_bp
from blueprints.account import account_bp
from blueprints.transaction import transaction_bp

Base.metadata.create_all(engine)
app = Flask(__name__)
CORS(app)

app.register_blueprint(customer_bp)
app.register_blueprint(account_bp)
app.register_blueprint(transaction_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
