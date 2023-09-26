import os.path
from api import app, db
from api.models import model_homework
from api.handlers import author
from api.handlers import quote

if not os.path.exists("./main.db"):
    with app.app_context():
        db.create_all()
