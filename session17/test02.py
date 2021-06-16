import threading
from time import sleep

def t1_func(s):
    sleep(2)
    print(s)

def t2_func(s, t1):
    sleep(1)
    print(s)
    t1.join()
    sleep(.5)
    print('bye')
    

t1 = threading.Thread(target=t1_func, args=("T1",))
t2 = threading.Thread(target=t2_func, args=("T2", t1))

t1.start()
t2.start()