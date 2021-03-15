
# mat = []
# for i in range(2):
#     mat.append([])
#     for j in range(2):
#         mat[i].append(int(input("Enter the {},{}th element: ".format(i + 1, j + 1))))
# print(mat)
mat = input("Enter your matrix: ")

mat = mat.replace('[', "")
mat = mat.replace(']', "")
mat = mat.replace(' ', "")
mat = mat.split(',')
# for i in range(len(mat)):
#     mat[i] = int(mat[i])
mat = [int(s) for s in mat]
print(mat)

det = mat[0]*mat[3] - mat[1]*mat[2]
reversed_mat = [
    [det* mat[3],det * (- mat[1])],
    [det * (- mat[2]), det * mat[0]]
]
print(reversed_mat)
