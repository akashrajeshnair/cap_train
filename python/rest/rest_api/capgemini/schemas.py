from marshmallow import Schema, fields, validate

class CustomerCreateSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    phone = fields.Str(required=True)

class CustomerSchema(CustomerCreateSchema):
    id = fields.Int(dump_only=True)

class AccountCreateSchema(Schema):
    account_number = fields.Str(required=True)
    customer_id = fields.Int(required=True)
    account_type = fields.Str(required=True, validate=validate.OneOf(["savings", "current"]))
    balance = fields.Int(required=True)

class AccountSchema(AccountCreateSchema):
    pass

class TransactionCreateSchema(Schema):
    amount = fields.Int(required=True)

class TransactionSchema(Schema):
    id = fields.Int(dump_only=True)
    account_number = fields.Str(required=True)
    txn_type = fields.Str(required=True)
    amount = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
