my_class = ['Mahdi', "Mohsen", 'Alireza', 'Radmehr']
my_grades = [18, 19, 13, 17]

# for name in my_class:
#     for grade in my_grades:
#         print(name, "-", grade)

for i in range(len(my_class)):
    my_str = my_class[i] + '=' + str(my_grades[i])
    print(my_str)