# Chapter -10 Object Oriented Programming

#       we make a class the sum two number.
'''
class Number:
    def sum(self):
        return self.a + self.b

num = Number()
num.a = 12
num.b = 34
s = num.sum()
print(s)
'''

#       we some two numbers normaly.
# a = 12
# b = 34
# print("The sum of a and b is ", a+b)


#       we write class function in PascalCase.
'''
PascalCase
EmployeeName --> PascalCase

camelCase
isNumeric, isFloatOrInt --> camelCase
'''

#       print simply some data with using class
'''
class RailwayFrom:
    fromType = "RailwayFrom"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

harrysApplication = RailwayFrom()
harrysApplication.name = "Harry"
harrysApplication.train = "Rajdhani Express"

harrysApplication.printData()
'''

#       Class game example 
'''
class Remote():
    pass

class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass
    
remote1 = remote()
player1 = Player()
if remote1.isLeftPressed():
    player1.moveLeft()
'''

'''
class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajhi = Employee()

harry.salary = 300
rajhi.salary = 400

print(harry.company)
print(rajhi.company)
Employee.company = "YouTube"
print(harry.company)
print(rajhi.company)

print(harry.salary)
print(rajhi.salary)
'''

'''
class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()
#       Creating instance attribute salary for both the objects
# harry.salary = 300
# rajni.salary = 400
harry.salary = 45
print(harry.salary)
print(rajni.salary)

#       Below line throws an error as address is not present in instance / class
# print(rajni.address)
# print(harry.__dict__)
'''

# class Employee:
#     company = "Google"
#     def getSalary(self, signature):
#         # print("Salary is 100K")
#         # print(f"Salary is {self.salary}")

# #       use @staticmethod used if im not use self in function so useing this method
#     # @staticmethod
#     # def greet():
#     #     print("Good Morning, Sir")

# harry = Employee()
# # harry.salary = 10000
# # harry.getSalary() # Employee.getSalary(harry)

# # harry.greet()
# harry.time()

#---------------------

class Employee:
    company = "Google"
    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is creaded")

    def getDetails(self):
        print(f"The name of th employee is {self.name}")
        print(f"The salary of th employee is {self.salary}")
        print(f"The subunit of th employee is {self.subunit}")

harry = Employee("Harry", 100, "YouTube")
harry.getDetails()