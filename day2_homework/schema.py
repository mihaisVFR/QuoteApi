from marshmallow import Schema, fields


class LearnerSchema(Schema):
    uid = fields.Integer()
    name = fields.Str(required=True, error_messages={"messege": "Error name is required", "code": 400})
    final_test = fields.Bool(required=True, error_messages={"messege": "Error final_test is required", "code": 400})
