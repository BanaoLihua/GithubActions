from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('flask_todo.config')

db = SQLAlchemy(app)

from flask_todo.views import views