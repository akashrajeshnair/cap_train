from flask import Flask, jsonify

app = Flask(__name__)

student_data = {
    1: {"name": "Anu", "dept": "CSE", "year": 3},
    2: {"name": "Karti", "dept": "ECE", "year": 3},
    3: {"name": "Priya", "dept": "IT", "year": 3}
}

staff_data = {
    101: {"name": "Dr. Ravi", "subject": "DAA"},
    102: {"name": "Dr. Meena", "subject": "DBMS"},
    103: {"name": "Dr. Arun", "subject": "OS"}
}

@app.route('/students', methods=['GET'])
def get_all_students():
    try:
        return jsonify(student_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        print("Get all students called")

@app.route('/students/<int:student_id>')
def get_student_by_id(student_id):
    try:
        if student_id not in student_data:
            return jsonify({"error": "student not found"}), 500
        return jsonify({
            "student_id": student_id,
            "details": student_data[student_id]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        print("Get student by id called")

@app.route('/staff', methods=['GET'])
def get_all_staff():
    try:
        return jsonify(staff_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        print("Get all staff called")

@app.route('/staff/<int:staff_id>')
def get_staff_by_id(staff_id):
    try:
        if staff_id not in staff_data:
            return jsonify({"error": "staff not found"}), 500
        return jsonify({
            "staff_id": staff_id,
            "details": staff_data[staff_id]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        print("Get staff by id called")


if __name__ == '__main__':
    app.run(port=3000, debug=True)