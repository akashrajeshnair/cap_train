"""
create bank account
open bank account
deposit money
withdraw with balance check
account details
transaction history"""

from marshmallow import Schema, fields

class CustomerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone_number = fields.Str(required=True)

class AccountSchema(Schema):
    account_no = fields.Int(dump_only=True)
    customer_id = fields.Int(required=True)
    account_type = fields.Str(required=True)
    balance = fields.Int(required=True)

class TransactionSchema(Schema):
    id = fields.Int(dump_only=True)
    account_no = fields.Int(required=True)
    transaction_type = fields.Str(required=True)
    amount = fields.Int(required=True)
    date = fields.DateTime(required=True)
