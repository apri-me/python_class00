num = int(input("adad? "))

while num<0 :
    print("mojadad talash konid!!!")
    num = int(input("adad jadid? "))

for i in range(1, num+1) :
    n = i * str("*")
    print(n)
for i in range(num-1, 0, -1) :
    m = i * "*"
    print(m)
