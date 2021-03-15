
n = int ( input("Enter Your Number: ") )

while n < 0:
    print("Your number is negative")
    n = int ( input("Enter correct number: "))

# factorial
s = 1
for i in range(1, n + 1):
    s *= i
print(f"Factorial of {n} is {s}")