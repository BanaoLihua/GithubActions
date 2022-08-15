import re
from flask import Response, redirect, render_template, request, url_for
from flask_todo import app, db
from flask_todo.models.todos import Todo
from datetime import datetime

@app.route('/')
def index():
    all = Todo.query.order_by(Todo.id.asc()).all()
    tasks = Todo.query.order_by(Todo.id.asc()).filter(Todo.type=='task')
    task_cnt = Todo.query.filter(Todo.iscompleted==False, Todo.type=='task').count()
    questions = Todo.query.order_by(Todo.id.asc()).filter(Todo.type=='question')
    question_cnt = Todo.query.filter(Todo.iscompleted==False, Todo.type=='question').count()
    return render_template('index.html', tasks=tasks, questions=questions, task_cnt=task_cnt, question_cnt=question_cnt)

@app.route('/create', methods=['POST'])
def create():
    if request.form.get('type') == 'task':
        task = Todo(content=request.form.get('content'),
                    detail='sample',
                    iscompleted=False,
                    due=datetime.today() if request.form.get('due')=='' else request.form.get('due'),
                    type='task')
        db.session.add(task)
        db.session.commit()
    if request.form.get('type') == 'question':
        question = Todo(content=request.form.get('content'),
                    detail='sample',
                    iscompleted=False,
                    due=datetime.today() if request.form.get('due') == '' else request.form.get('due'),
                    type='question')
        db.session.add(question)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    todo = Todo.query.filter(Todo.id == request.form.get('id')).one()
    todo.content = request.form.get('content')
    todo.due = datetime.today() if request.form.get('due') == '' else request.form.get('due')
    db.session.merge(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    todo = Todo.query.filter(Todo.id==request.form.get('id')).one()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/check', methods=['POST'])
def check():
    is_completed = True if request.form.get('iscompleted') == 'true' else False
    todo = Todo.query.filter(Todo.id==request.form.get('id')).one()
    todo.iscompleted = is_completed
    db.session.merge(todo)
    db.session.commit()
    response = Response()
    response.status_code = 201
    return response
