# aza matrix
a = int(input("adad 1 radif 1 matrix? "))
b = int(input("adad 2 radif 1 matrix? "))
c = int(input("adad 1 radif 2 matrix? "))
d = int(input("adad 2 radif 2 matrix? "))

matrix = [[a, b], [c, d]]

print(matrix)
j = input("aya matrix shoma hamine? y/n? ")
while (j == "n") :
    print("matrix ra mojadad vared konid: ")
    a = int(input("adad 1 radif 1 matrix? "))
    b = int(input("adad 2 radif 1 matrix? "))
    c = int(input("adad 1 radif 2 matrix? "))
    d = int(input("adad 2 radif 2 matrix? "))
    
    matrix = [[a, b], [c, d]]
    
    print(matrix)
    j = input("aya matrix shoma hamine? y/n? ")
    if (j == "y") :
        break


# aza matrix makoos
A,B,C,D = b,a,(-c),(-d)

matrix_makoos = [[A, B], [C, D]]

print(f"matrix makoose matrix {matrix} barabar ba: {matrix_makoos}")