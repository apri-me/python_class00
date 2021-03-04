
mat1 = [ [1, 3, -2], [2, 4, 6] , [-5, -2, 1] ]

mat2 = [ [5, -3, 12], [6, -2, 3], [8, 4, -6] ]

mat3 = []

# mat3 = [ [] ]

for i in range(3):
    mat3.append([])
    for j in range(3):
        mat3[i].append( mat1[i][j] + mat2[i][j] )


for row in mat3:
    print(row)
