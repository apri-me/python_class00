
# def times_two(a):
#     return a * 2

# def somename(x):
#     return 0 if x[-1] == 'i' else 1


li = [4, 2, 3, 1]
li.sort()
print(li)

cl = ['mohsen', 'radmehr', 'mahdi', 'alireza']

cl.sort(key=len)

print(cl)

print(max(cl, key=len))