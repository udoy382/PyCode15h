# Chapter -11 Inheritance

# ------------------------------------
#       Single inheritance
# ------------------------------------
'''
class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"
    # company = "YouTube"
    def getLanguage(self):
        print("The language is {self.language}")

    def showDetails(self):
        print("This is an Programmer")

e = Employee()
e.showDetails()

p = Programmer()
p.showDetails()
print(p.company)
'''
# ------------------------------------
#       Multiple inheritance
# ------------------------------------
'''
class Freelancer:
    company = "Fiverr"
    level = 0

class Employee:
    company = "Visa"
    eCode = 120

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Freelancer, Employee):
    name = "Rohit"

p = Programmer()

p.upgradeLevel()
print(p.level)]
print(p.company)
'''
# ------------------------------------
#       Multilevel inheritance
# ------------------------------------
'''
class Person:
    country = "Bangladehs"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"
    country = "India"
    def getsalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so I am breathing")

class Programmer(Employee):
    company = "Fiver"

    def getsalary(self):
        print(f"No salary to programmer")

    def takeBreath(self):
        print("I am an Programmer so I am  breathing + +")

p = Person()
# print(p.company) # throws an error
p.takeBreath()

e = Employee()
print(e.company)
e.takeBreath()
pr = Programmer()
pr.takeBreath()
print(pr.country)
'''
# ------------------------------------
#       Super function
# ------------------------------------
'''
class Person:
    country = "Bangladehs"

    def __init__(self):
        print("Initilizing Person...\n")

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        print("Initilizing Employee...\n")

    def getsalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am breathing")

class Programmer(Employee):
    company = "Fiver"

    def __init__(self):
        super().__init__()
        print("Initilizing Programmer...\n")

    def getsalary(self):
        print(f"No salary to programmer")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Programmer so I am  breathing + +")

# p = Person()
# p.takeBreath()

e = Employee()
e.takeBreath()

# pr = Programmer()
# pr.takeBreath()
'''
# ------------------------------------
#       class methods
# ------------------------------------
'''
class Employee:
    company = "camel"
    salary = 100
    location = "Delhi"

    # def changeSalary(self, sal):
    #     self.__class__.salary = sal

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)
'''
# ------------------------------------
#       property decorator
# ------------------------------------
'''
class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 400
    # totalSalary = 6100

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self, val):
        salarybonus = val - self.salary


e = Employee()
print(e.totalSalary)
e.totalSalary = 5800
print(e.salary)
print(e.salarybonus)
'''
# ------------------------------------
#       operator overloading
# ------------------------------------
'''
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Lets multiply")
        return self.num * num2.num

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)
'''
# ------------------------------------
#       other dunder methods
# ------------------------------------
'''
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Lets multiply")
        return self.num * num2.num

    def __str__(self):
        return f"Decimal Number: {self.num}"

    def __len__(self):
        return 1

n = Number(9)
print(n)
print(len(n))
'''