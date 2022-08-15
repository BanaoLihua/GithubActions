from flask_todo import db
from datetime import datetime


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    detail = db.Column(db.String)
    iscompleted = db.Column(db.Boolean)
    due = db.Column(db.Date)
    type = db.Column(db.String)
    createdat = db.Column(db.Date)

    def __init__(self, content, detail, iscompleted, due, type):
        self.content = content
        self.detail = detail
        self.iscompleted = iscompleted
        self.due = due
        self.type = type
        self.createdat = datetime.today()
