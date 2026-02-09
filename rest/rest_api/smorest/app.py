from flask import Flask
from flask_smorest import Api, Blueprint
from flask.views import MethodView
from marshmallow import Schema, fields

app = Flask(__name__)

app.config["API_TITLE"] = 'Student API'
app.config["API_VERSION"] = 'v1'
app.config["OPENAPI_VERSION"] = '3.0.3'
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

class StudentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    dept = fields.Str(required=True)

blp = Blueprint(
    'students',
    __name__,
    description = "Student CRUD Operations"
)

students = []

@blp.route('/students')
class StudentList(MethodView):
    @blp.response(200, StudentSchema(many=True))
    def get(self):
        """Get all students"""
        return students
    
    @blp.arguments(StudentSchema)
    @blp.response(201, StudentSchema)
    def post(self, student_data):
        """Create a new student"""
        student_data['id'] = len(students)+1
        students.append(student_data)
        return student_data

@blp.route('/students/<int:id>') 
class Student(MethodView):
    @blp.arguments(StudentSchema)
    @blp.response(201, StudentSchema)
    def put(self, student_data, id):
        """Update a student"""
        for s in students:
            if s["id"] == id:
                s.update(student_data)
        return student_data
    
    def delete(self, id):
        """Delete a student"""
        global students
        for s in students:
            if s["id"] == id:
                students = [s for s in students if s["id"]!= id]
        return {"message": "deleted successfully"}, 200

    
api.register_blueprint(blp)

if __name__ == '__main__':
    app.run(port=3000, debug=True)