from flask import Blueprint, request, jsonify
from db.models import Employee, Base
from db.database import session_local, engine

employee_bp = Blueprint('employee', __name__, url_prefix='/employee')

@employee_bp.route('/view-employee/<int:id>', methods=['GET'])
def get_employee_details(id):
    with session_local() as session:
        employee = session.query(Employee).filter_by(id=id).first()
        if employee:
            return jsonify({
                "id": employee.id,
                "salary": employee.salary,
                "annual_salary": employee.annual_salary,
                "pf": employee.pf
            })
        
@employee_bp.route('/create-employee', methods=['POST'])
def create_employee_details():
    data = request.json
    salary = data.get('salary')
    annual_salary = data.get('annual_salary')
    pf = data.get('pf')

    if not salary or not annual_salary or not pf:
        return jsonify({"error": "missing fields"}), 400
    
    auth_header = request.headers.get('Authorization')

    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Authorization token required"}), 401

    with session_local() as session:
        new_employee = Employee(salary=salary, annual_salary=annual_salary, pf=pf)
        session.add(new_employee)
        session.commit()

        return jsonify({
            "message": "Employee created successfully",
            "employee_id": new_employee.id
        })

@employee_bp.route('/update-employee/<int:id>', methods=['PUT'])
def update_employee_details(id):
    data = request.json
    if not data:
        return jsonify({"error": "missing fields"}), 400
    
    auth_header = request.headers.get('Authorization')

    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Authorization token required"}), 401
    
    with session_local() as session:
        employee = session.query(Employee).filter_by(id=id).first()
        
        if not employee:
            return jsonify({"error": "Employee does not exist"}), 404

        if 'salary' in data:
            employee.salary = data.get('salary')
        if 'annual_salary' in data:
            employee.annual_salary = data.get('annual_salary')
        if 'pf' in data:
            employee.pf = data.get('pf')

        session.commit()

        return jsonify({
                "id": employee.id,
                "salary": employee.salary,
                "annual_salary": employee.annual_salary,
                "pf": employee.pf
        })
    
@employee_bp.route('/delete-employee/<int:id>', methods=['DELETE'])
def delete_employee_details(id):
    auth_header = request.headers.get('Authorization')

    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Authorization token required"}), 401

    with session_local() as session:
        employee = session.query(Employee).filter_by(id=id).first()
        
        if not employee:
            return jsonify({"error": "Employee does not exist"}), 404
        
        session.delete(employee)
        session.commit()
        return jsonify({"message": "employee deleted"})
        
