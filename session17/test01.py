import threading
from time import sleep

def t1_func(s):
    sleep(2)
    print(s)

t1 = threading.Thread(target=t1_func, args=("Hello",))

print("t1 is starting")
t1.start()
sleep(2)
print('bye')