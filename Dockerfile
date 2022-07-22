FROM python:alpine

WORKDIR /todo_app

COPY ./todo_app /todo_app

RUN python -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org pip python-dotenv

RUN pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org --upgrade pip

RUN pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org Flask SQLAlchemy flask_sqlalchemy psycopg2-binary

CMD ["python", "app.py"]