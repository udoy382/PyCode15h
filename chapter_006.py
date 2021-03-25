# Chapter -6 Conditional Expressions

# -------------------------------------------
    #   if-elif-else ladder in python
# -------------------------------------------

# a = 75
# if(a>3):
#     print('The value of a is greater then 3')
# elif(a>7):
#     print("The value of a is greater then 7")
# elif(a>17):
#     print("The value of a is greater then 17")
# elif(a>27):
#     print("The value of a is greater then 27")
# else:
#     print("The value is not greater then 3 or 7")

# print("Done")

# ----------------------------------------
#       Multiple if statements
# ----------------------------------------

# a = 24
# if(a<3):
#     print('The value of a is greater then 3')
# if(a>7):
#     print("The value of a is greater then 7")
# if(a>30):
#     print("The value of a is greater then 17")
# if(a>27):
#     print("The value of a is greater then 27")
# else:
#     print("The value is not greater then 3 or 7")

# Quiz...

# age = int(input("Enter the age: "))
# if age<18:
#     print("No")
# elif age==18:
#     print("Maybe")
# else:
#     print("Yes")

# ---------------------------------
#       Logical operators
# ---------------------------------

# age = int(input("Enter your age: "))
# if (age>34 and age<56):
#     print("You can work with us")
# else:
#     print("You can not work with us")


# age = int(input("Enter your age: "))
# if (age>34 or age<56):
#     print("You can work with us")
# else:
#     print("You can not work with us")

# ------------------------
#       in_and_is
# ------------------------

# a = None
# if (a is None):
#     print("Yes")
# else:
#     print("No")


# a = [2, 34, 65, 77, 45]
# print(45 in a)

# ------------

a = 4
if(a==7):
    print("yes")
elif(a>56):
    print("no and yes")
else:
    print("im optional")