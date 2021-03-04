name = input("What is your name? ")
age = int(input("What is your age: "))

# print("hello " + name + " your age is " + str(age))

# print(f'hello {name} {{}} your age is {age}')

# print("hello {} your age is {}{{}}".format(name, age))

print("hello %s your %i" % (name, age) )