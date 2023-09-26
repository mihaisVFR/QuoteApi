from api import db


class Learner(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    final_test = db.Column(db.Boolean, nullable=False)

    def __init__(self, uid, name, final_test):
        self.uid = uid
        self.name = name
        self.final_test = final_test

    def __repr__(self):
        return f"Learner({self.uid}): {self.name}|{self.final_test}"

