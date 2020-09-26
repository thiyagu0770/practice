class Employee():
    name = "Ravi"
    print(name)
    def __init__(self):
        Employee.a = 523
        print(Employee.a)
    def m1(self):
        Employee.b = 578
        print(Employee.b)
        print(Employee.a)
        print(Employee.name)
    @classmethod
    def m2(cls):
        Employee.c = 756
        print(Employee.name)
        print(Employee.a)
        print(Employee.b)
        print(Employee.c)
    @classmethod
    def m3(cls):
        Employee.d = 435
        print(Employee.name)
        print(Employee.a)
        print(Employee.b)
        print(Employee.c)
        print(Employee.d)
Employee.f=278
e=Employee()
print(Employee.f)
e.m1()
e.m2()
e.m3()



