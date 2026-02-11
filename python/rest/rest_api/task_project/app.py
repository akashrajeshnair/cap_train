from flask import Flask
from flask_cors import CORS
from task_project.api.authentication import auth_bp
from task_project.api.tasks import task_bp
from task_project.api.projects import project_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_bp)
app.register_blueprint(task_bp)
app.register_blueprint(project_bp)

if __name__ == '__main__':
    app.run(port=3000, debug=True)