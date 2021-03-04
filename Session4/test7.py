from prettytable import PrettyTable

pt = PrettyTable( ["First Name", 'Last Name', "grade"] )

pt.add_row( ['Mohsen', "RahimBakhsh", 19] )

pt.add_row( ['Alireza', "AFroozi", 18])

pt.add_row( ['Cristiano', 'Ronaldo', 20] )

print(pt)