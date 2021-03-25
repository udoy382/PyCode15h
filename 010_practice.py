# -------------------------------------
# Chapter -10 practice set...
# -------------------------------------

#  (1)

'''
class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name}, and the product is {self.product}")

udoy = Programmer("Saifur Rahman Udoy", "SKype")
alka = Programmer("Alka", "GitHub")

udoy.getInfo()
alka.getInfo()
'''

#  (2)

'''
class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    def squareRoot(self):
        print(f"The value of {self.number} square root is {self.number **0.5}")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number **3}")

a = Calculator(3)
a.square()
a.squareRoot()
a.cube()
'''

#  (3)

'''
class Sample:
    a = "Udoy"

obj = Sample()
obj.a = "Vikky"
# Sample.a = "Vikky" # this methed change class object.
print(Sample.a)
print(obj.a)
# print(Sample.__dict__)
# print(obj.__dict__)
'''
#  (4)

'''
class Hey_Greet:
    def greet():
        print(f"*****Hey greet welcome to the our world*****")

Hey_Greet.greet()
'''

#  (5)

'''
class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")

    def fareInfo(self):
        print(f"The price of ticket is : $ {self.fare}")

    def bookTicket(self):
        if (self.seats>0):
            print("Your ticket has benn booked! your seat number is {self.seats}")
            self.seats = self.seats -1
        else:
            print("Sorry this train is full! try it tatkal")

    def cancelTicket(self, seatNo):
        pass

intercity = Train("intercity Express: 14015", 90, 2)

# intercity.getStatus()
# intercity.fareInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
'''

#  (6)

'''
class Sample:
    def __init__(udoy, name):
        udoy.name = name

obj = Sample("Harry")
print(obj.name)
'''
