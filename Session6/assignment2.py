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

salary_per_hour = int ( input("How much you pay per hour? ") )

my_dict = dict (zip (employees, hours) )

pt = prettytable.PrettyTable( ["Name", "Hours", "Salary"] )

for name, h in my_dict.items():
    pt.add_row( [name, h, h * salary_per_hour] )

print(pt)