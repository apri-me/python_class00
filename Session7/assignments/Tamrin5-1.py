n = int(input ("Enter a number:"))
start = []

for i in range (n):
    start.append("*")
    print("".join(start))

start.pop(-1)
for i in range (n-2, -1, -1):
    print ("".join(start))
    start.pop(i)