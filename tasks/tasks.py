from celery import Celery
from .worker import app


@app.task
def add(x, y):
    return x + y