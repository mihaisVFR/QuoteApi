from marshmallow import Schema, fields, validate
from api.models.model_homework import Learner


class LearnerSchema(Schema):
    uid = fields.Integer()
    name = fields.Str(required=True, error_messages={"required": "name is required", "code": 400},
                      validate=[validate.Length(max=30)])
    final_test = fields.Bool(required=True, error_messages={"required": "final_test is required", "code": 400},
                             data_key="olympic")


