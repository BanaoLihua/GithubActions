from flask_todo import app
from dotenv import load_dotenv
load_dotenv()

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# config に DATABASE_URL が設定されている前提
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)

# モデルのインポート
from flask_todo.models import Todo

# 本番用: 初回起動時にテーブル作成
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("PORT") , debug=True)
