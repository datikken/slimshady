from celery import Celery

app = Celery('tasks', backend='rpc://', broker='pyamqp://user:password@localhost//')

@app.task
def add(x, y):
    return x + y