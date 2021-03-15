# print()
# print('hello')
# print('hello', 'world')

def mult(*args, b=4, c = 5):
    # args = [...]
    p = 1
    for a in args:
        p *= a
    p += b - c
    return p

print(mult(2, 3, 4, 5, 8, b=5, c=2))
