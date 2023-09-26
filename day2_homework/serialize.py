from api.models.model_homework import Learner
from day2_homework.schema import LearnerSchema
from api import app


def serialize_learner(learner_id=1, many=False):
    with app.app_context():
        if many:
            learner = Learner.query.all()
            learner_schema = LearnerSchema(many=True)
        else:
            learner = Learner.query.get(learner_id)
            learner_schema = LearnerSchema()

        result = learner_schema.dump(learner)
        return result


def tests():
    print(serialize_learner(many=True), type(serialize_learner(many=True)))
    print(serialize_learner(), type(serialize_learner()))

