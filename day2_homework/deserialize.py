from schema import LearnerSchema
from serialize import serialize_learner
from api import app


def to_txt():
    learner = serialize_learner()
    learners = serialize_learner(many=True)
    with open("tmp.txt", "w", encoding="utf-8") as f:
        print(learners, file=f)
        print(learner, file=f)


def deserialize_learner(many=False):
    with app.app_context():
        with open("tmp.txt", "r", encoding="utf-8") as f:
            string = f.readlines()
            if many:
                json_data = string[0].replace('True', '"True"') .replace("'", '"').replace("False", '"False"')
                schema = LearnerSchema(many=True)
            else:
                json_data = string[1].replace('True', '"True"') .replace("'", '"')
                schema = LearnerSchema()

            return schema.loads(json_data)


def tests():
    print(deserialize_learner(many=True))
    print(deserialize_learner(), type(deserialize_learner()))