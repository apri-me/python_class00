def factorial(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    #
    return s

f = factorial(5)
print(f)
