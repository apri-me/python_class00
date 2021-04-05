from math import sqrt

def is_prime(m):
    if m == 1:
        return False
    for x in range(2, int(sqrt(m)) + 1):
        if m % x == 0:
            return False
    return True


def prime_numbers(n):
    li = []
    for m in range(1, n):
        if is_prime(m):
            li.append(m)
    return li

print(prime_numbers(1000))