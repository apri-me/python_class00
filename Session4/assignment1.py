n = int(input())
m = int(input())

tn = n
tm = m
sn = ""
sm = ""
while(tn > 0):
    sn += str(tn % 10)
    tn = tn // 10

sn = int(sn)

while(tm > 0):
    sm += str(tm % 10)
    tm = tm // 10

sn = int(sn)
sm = int(sm)

if (sn > sm):
    print(n, ">", m)
elif (sn < sm):
    print(n, "<", m)
else:
    print(n, "=", m)