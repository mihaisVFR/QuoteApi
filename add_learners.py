from api import db, app
from api.models.model_homework import Learner

learners = [
    Learner("1", "Petr", True),
    Learner("2", "Alex", True),
    Learner("3", "Ivan", False),
    Learner("4", "Tom", True)
]
with app.app_context():
    for learner in learners:
        db.session.add(learner)
        db.session.commit()



