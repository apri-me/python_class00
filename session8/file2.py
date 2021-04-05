

f = open('filename.txt')

for line in f:
    words = line.split()
    print(*words, sep=", ")

f.close()