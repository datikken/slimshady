import asyncio
from celery import Celery

app = Celery('tasks', backend='rpc://', broker='pyamqp://user:password@localhost//')

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

async def sum(a, b):
    res = a + b
    return res


@app.task
def add(x, y):
  asyncio.run(sum(x, y))


if __name__ == '__main__':
    app.start()