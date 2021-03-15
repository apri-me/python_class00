import prettytable


n = int ( input("Number of employees: ") )
employees = []

for i in range(n):
    emp = input("Emplyee number {}: ".format(i + 1))
    employees.append(emp)

hours = []
for i in range(n):
    h = float ( input("Work hours of Employee {}: ".format(i + 1)))
    hours.append(h)

factors = []
for i in range(n):
    f = int ( input("How much employee {} gets per hour: ".format(i + 1)))
    factors.append(f)

my_list = list ( zip (hours, factors) )

print(my_list)



my_dict = dict (zip (employees, hours, factors) )

# pt = prettytable.PrettyTable( ["Name", "Hours", "Salary"] )

# for c in my_list:
#     pt.add_row([c[0] , c[1], c[1] * c[2]] )

# print(pt)