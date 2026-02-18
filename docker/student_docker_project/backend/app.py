from flask import Flask, request
from sqlalchemy.orm import sessionmaker
from database import engine
from models import Student

app = Flask(__name__)
Session = sessionmaker(bind=engine)

@app.route("/add", methods=["POST"])
def add_student():
    name = request.form["name"]
    email = request.form["email"]

    session = Session()
    student = Student(name=name, email=email)
    session.add(student)
    session.commit()
    session.close()

    return "Student Added Successfully"

@app.route("/")
def home():
    return "Backend Running"

app.run(host="0.0.0.0", port=5000)
