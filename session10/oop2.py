class Employee:
    raise_factor = 1.06
    num_of_emps = 0
    list_of_emps = []
    def __init__(self, fname, lname, pay=10000):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = "{}.{}@gle.com".format(fname, lname)
        Employee.num_of_emps += 1
        Employee.list_of_emps.append(self)

    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

    def raise_pay(self):
        self.pay = int(self.pay * Employee.raise_factor)

    @classmethod
    def set_raise_factor(cls, new_factor):
        cls.raise_factor = new_factor

    @classmethod
    def init_by_fullname(cls, name):
        firstname = name.split()[0]
        lastname = name.split()[1]
        return cls(firstname, lastname)

    @staticmethod
    def congratulate():
        print("Eydetun Mobarak")


emp1 = Employee("alireza", "afroozi")

emp2 = Employee.init_by_fullname("Mohsen Rahimbakhsh")

print(emp2.fname)
print(emp2.lname)
print(emp2.pay)

# print(emp1.pay)
