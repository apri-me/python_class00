def print_names(*args,**kwargs):
    print(args)
    for k, v in kwargs.items():
        print(f"{k} is {v}")
    print(type(args))
    print(type(kwargs))

print_names(1, 2, 4, 3,alireza='afroozi', mahdi='rahimbakhsh')
