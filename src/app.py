from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from flask import Flask

app = Flask(__name__)

app.config.from_pyfile("config.py")

db = SQLAlchemy(app)

csrf = CSRFProtect(app)

if __name__ == "__main__":
    from apis.views import *

    app.run(debug=True)
