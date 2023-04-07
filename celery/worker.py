from tasks import add
from time import sleep

result = add.apply_async((4,4))

print('test')
print(result.get())
print('green')
