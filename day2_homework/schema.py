from marshmallow import Schema, fields, validate
from api.models.model_homework import Learner


class LearnerSchema(Schema):
    uid = fields.Integer()
    name = fields.Str(required=True, error_messages={"required": "name is required", "code": 400},
                      validate=[validate.Length(max=30)])
    final_test = fields.Bool(required=True, error_messages={"required": "final_test is required", "code": 400})

# не разобрался как заменить аргумент класса final_test на olympic

""" Задание:

Выведите словарь в стандартный вывод
Sample Output:
{'olympic': True, 'uid': 10, 'name': 'Vlad'}

#class Learner(db.Model):
#    uid = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String, nullable=False)    
#    final_test = db.Column(db.Boolean, nullable=False)

from marshmallow import Schema, fields

class LearnerSchema(Schema):
    ....

learner = Learner(name='Vlad', uid=10, olympic=True)

print(....)
"""
# learner = Learner(name='Vlad', uid=10, olympic=True)
# print(learner)


