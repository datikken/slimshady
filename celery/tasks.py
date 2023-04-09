from celery import Celery

app = Celery('tasks', backend="redis", broker='pyamqp://user:password@localhost//')
app.conf.result_backend = 'redis://:sOmE_sEcUrE_pAsS@localhost:6379/0'
app.conf.update(
    result_expires=3600,
)

def sum(a, b):
    res = a + b
    with open("polution.txt", "w") as file:
        file.write(str(res))
    return res

@app.task
def add(x, y):
  return sum(x, y)

if __name__ == '__main__':
    app.start()