class Employee:
    raise_factor = 1.06
    num_of_emps = 0
    list_of_emps = []
    def __init__(self, fname, lname, pay):
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

if __name__ == '__main__':
    # print(Employee.num_of_emps)
    emp_1 = Employee("alireza", "afroozi", 5000)
    # print(Employee.num_of_emps)
    # emp_2 = Employee('cristiano', 'ronaldo', 100000)
    # print(Employee.num_of_emps)
    Employee.set_raise_factor(1.1)
    # emp_1.set_raise_factor(1.08)
    print(Employee.raise_factor)


    # print(Employee.list_of_emps[1].fullname())
