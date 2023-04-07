from celery import Celery
from time import sleep

tg = Celery('tasks', backend='rpc://', broker='pyamqp://user:password@localhost//')

@tg.task
def add(x, y):
    sleep(1)
    return x + y