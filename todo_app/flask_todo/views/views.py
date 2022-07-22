import re
from flask import Response, redirect, render_template, request, url_for
from flask_todo import app, db
from flask_todo.models.tasks import Task
from flask_todo.models.questions import Question
from datetime import datetime

@app.route('/')
def index():
    tasks = Task.query.order_by(Task.id.asc()).all()
    task_cnt = Task.query.filter(Task.iscompleted==False).count()
    questions = Question.query.order_by(Question.id.asc()).all()
    question_cnt = Question.query.filter(Question.iscompleted==False).count()
    return render_template('index.html', tasks=tasks, questions=questions, task_cnt=task_cnt, question_cnt=question_cnt)

@app.route('/create', methods=['POST'])
def create():
    if request.form.get('type') == 'task':
        task = Task(content=request.form.get('content'),
                    detail='sample',
                    iscompleted=False,
                    due=datetime.today() if request.form.get('due')=='' else request.form.get('due'))
        db.session.add(task)
        db.session.commit()
    if request.form.get('type') == 'question':
        question = Question(content=request.form.get('content'),
                    detail='sample',
                    iscompleted=False,
                    due=datetime.today() if request.form.get('due') == '' else request.form.get('due'))
        db.session.add(question)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    if request.form.get('type') == 'task':
        task = Task.query.filter(Task.id==request.form.get('id')).one()
        task.content = request.form.get('content')
        task.due = datetime.today() if request.form.get('due') == '' else request.form.get('due')
        db.session.merge(task)
        db.session.commit()
    if request.form.get('type') == 'question':
        question = Question.query.filter(Question.id == request.form.get('id')).one()
        question.content = request.form.get('content')
        question.due = datetime.today() if request.form.get('due') == '' else request.form.get('due')
        db.session.merge(question)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    if request.form.get('type') == 'task':
        task = Task.query.filter(Task.id==request.form.get('id')).one()
        db.session.delete(task)
        db.session.commit()
    if request.form.get('type') == 'question':
        question = Question.query.filter(Question.id==request.form.get('id')).one()
        db.session.delete(question)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/check', methods=['POST'])
def check():
    if request.form.get('type') == 'task':
        is_completed = True if request.form.get('iscompleted') == 'true' else False
        task = Task.query.filter(Task.id==request.form.get('id')).one()
        task.iscompleted = is_completed
        db.session.merge(task)
        db.session.commit()
    if request.form.get('type') == 'question':
        is_completed = True if request.form.get('iscompleted') == 'true' else False
        question = Question.query.filter(Question.id==request.form.get('id')).one()
        question.iscompleted = is_completed
        db.session.merge(question)
        db.session.commit()
    response = Response()
    response.status_code = 201
    return response