from api import app
from config import Config
from api.handlers import author
from api.handlers import quote

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)
