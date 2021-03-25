# Chapter -8 Functions & Recursion


# def persent(marks):
#     return ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100

# marks1 = [45, 78, 86, 77]
# percentage1 = persent(marks1)

# marks2 = [75, 98, 88, 78]
# percentage2 = persent(marks2)

# print(percentage1, percentage2)

# Quick Quiz...

# def great(name):
#     print("Good Day " + name)

# great("Udoy")

#------------------

def mySum(num1, num2):
    return num1 + num2

s = mySum(6, 32)
# print(s)

# ----------------------------------
#       default arguments
# ----------------------------------

# def great(name="stranger"):
#     print("Good Day " + name)

# great("Udoy")
# great()

# --------------------------
#       Recursion
# --------------------------

# n! = 1 * 2 * 4 * 4...*n
# n! = *n (n-1)!

#-------------------

# n = 4
# product = 1
# for i in range(n):
#     product = product * (i+1)

# print(product)

#------------------

# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return product
# f = factorial_iter(5)
# print(f)

#-------------------

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)

f = factorial_recursive(5)
print(f)