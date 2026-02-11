from flask_smorest import Blueprint
from flask.views import MethodView
from banking_system.schema import CustomerSchema

customer_blp = Blueprint(
    'customers',
    __name__,
    description = "Customer CRUD Operations"
)

customers = []

@customer_blp.route('/customers')
class CustomerList(MethodView):
    @customer_blp.response(200, CustomerSchema(many=True))
    def get(self):
        """Get all customers"""
        return customers
    
    @customer_blp.arguments(CustomerSchema)
    @customer_blp.response(201, CustomerSchema)
    def post(self, customer_data):
        """Create a new customer"""
        customer_data['id'] = len(customers)+1
        customers.append(customer_data)
        return customer_data

@customer_blp.route('/customers/<int:id>') 
class Customer(MethodView):
    @customer_blp.response(200, CustomerSchema)
    def get(self, id):
        """Get a customer by id"""
        for c in customers:
            if c["id"] == id:
                return c
        return {"message": "Customer not found"}, 404
    
    @customer_blp.arguments(CustomerSchema)
    @customer_blp.response(201, CustomerSchema)
    def put(self, customer_data, id):
        """Update a customer"""
        for c in customers:
            if c["id"] == id:
                c.update(customer_data)
        return customer_data
    
    def delete(self, id):
        """Delete a customer"""
        global customers
        for c in customers:
            if c["id"] == id:
                customers = [c for c in customers if c["id"]!= id]
        return {"message": "deleted successfully"}, 200

    
