

def mul(arg1, *args):
    # args is a list of arguments
    p = arg1
    for i in args:
        p *= i
    return p

if __name__ == '__main__':
    print(mul(2, 4, 6))