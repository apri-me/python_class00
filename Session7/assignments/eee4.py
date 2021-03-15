mat1 = input("Enter your 1st matrix: ")

mat1 = mat1.replace('[', "")
mat1 = mat1.replace(']', "")
mat1 = mat1.replace(' ', "")
mat1 = mat1.split(',')
mat1 = [int(s) for s in mat1]

mat2 = input("Enter your 2nd matrix: ")

mat2 = mat2.replace('[', "")
mat2 = mat2.replace(']', "")
mat2 = mat2.replace(' ', "")
mat2 = mat2.split(',')
mat2 = [int(s) for s in mat2]

a = mat1[0] * mat2[0] + mat1[1] * mat2[2]
b = mat1[0] * mat2[1] + mat1[1] * mat2[3]
c = mat1[2] * mat2[0] + mat1[3] * mat2[2]
d = mat1[2] * mat2[1] + mat1[3] * mat2[3]

print( [[a,b], [c, d]])
