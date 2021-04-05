import math
print("You are importing from my_module")
print(__name__)

def factorial(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


def abs(a):
    if a >= 0:
        return a
    return -1 * a


def fib(n):
    li = [0, 1]
    for i in range(2, n + 1):
        li.append(li[i - 1] + li[i - 2])
    return li[n]


if __name__ == "__main__":
    print("It's main")


