from flask import Flask
from api.login import auth_bp
from api.employee import employee_bp

app = Flask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(employee_bp)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
