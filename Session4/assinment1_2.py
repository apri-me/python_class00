n = input()
m = input()

sn = n[::-1]
sm = m[::-1]

if (sn > sm):
    print(n, ">", m)
elif (sn < sm):
    print(n, "<", m)
else:
    print(n, "=", m)