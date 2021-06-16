import threading
import time
import numpy

summation = []

def func(l1, l2):
    global summation
    out = []
    for i in range(len(l1)):
        out.append(l1[i] + l2[i])
    summation += out

li1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li2 = li1[::-1]

t1 = threading.Thread(target=func, args=(li1[:5], li2[:5]))
t2 = threading.Thread(target=func, args=(li1[-5:], li2[-5:]))

start = time.process_time()
t1.start()
t2.start()

t1.join()
t2.join()
end = time.process_time()

print(summation)
print((end - start))
print()

start = time.process_time()
out = []
for i in range(len(li1)):
    out.append(li1[i] + li2[i])
print(out)
end = time.process_time()
print((end - start))
print()