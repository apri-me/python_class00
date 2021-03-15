import math

def fibonacci(n):
    li = [0, 1]
    for i in range(2, n + 1):
        li.append(li[i - 1] + li[i - 2])
    return li[n]
