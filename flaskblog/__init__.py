from flask import Flask
from flask_sqlalchemy import SQLAlchemy

######################################################################
# App configurations.  Duh.
app = Flask(__name__)
app.config['SECRET_KEY'] = '4038aa7c4030dc7c502bf6847351f6ff'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Need to learn about SQALCHEMY Track modifications.
db = SQLAlchemy(app)

from flaskblog import routes
