from tasks import add
from time import sleep

result = add.delay(4, 5)

print('test')
print(result.get())
