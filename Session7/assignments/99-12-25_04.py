# aza matrix 1
a1 = int(input("adad 1 radif 1 matrix 1? "))
b1 = int(input("adad 2 radif 1 matrix 1? "))
c1 = int(input("adad 1 radif 2 matrix 1? "))
d1 = int(input("adad 2 radif 2 matrix 1? "))

# aza matrix 2
a2 = int(input("adad 1 radif 1 matrix 2? "))
b2 = int(input("adad 2 radif 1 matrix 2? "))
c2 = int(input("adad 1 radif 2 matrix 2? "))
d2 = int(input("adad 2 radif 2 matrix 2? "))

# aza zarb
A = (a1 * a2) + (b1 * c2)
B = (a1 * b2) + (b1 * d2)
C = (c1 * a2) + (d1 * c2)
D = (c1 * b2) + (d1 * d2)

matrix_zarb = [[A, B], [C, D]]

print(f"zarb matrix1 dar matrix2 barabar ast ba: {matrix_zarb}")