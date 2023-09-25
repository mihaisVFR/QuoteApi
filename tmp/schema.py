from marshmallow import Schema, fields

class AuthorSchema(Schema):
    id = fields.Integer()
    name = fields.Str(required=True,error_messages={"messege": "Error name is required", "code": 400})
    email = fields.Email(required=True, error_messages={"required": "Error email is required"})
