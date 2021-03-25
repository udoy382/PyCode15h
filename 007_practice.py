# -------------------------------------
# Chapter -7 practice set...
# -------------------------------------

#  (1)

# num = int(input("Enter the number: "))
# for i in range(1, 11):
#     # print(str(num) + " X " + str(i) + "=" + str(i*num))
#     print(f"{num} X {i} = {num*i}")

#  (2)

# l1 = ["Harry", "Udoy", "Rahul", "Sohan", "Sachin"]

# for name in l1:
#     if name.startswith("S"):
#         print("Hello " + name)

#  (3)

# num = int(input("Enter the number: "))
# prime = True

# for i in range(2, num):
#     if (num%i == 0):
#         prime = False
#         break

# if prime:
#     print("This number is prime")
# else:
#     print("This number is not prime")


#  (4)
# ---------------------
#       Factorial
# ---------------------

# n! = 1 * 2 * 3 * 4 *......* n

# 5! = 1 * 2 * 3 * 4* 5

# num = int(input("Enter the number: "))
# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial * i

# print(f"The factorial of {num} is {factorial}")

#  (5)

# n = 4

# for i in range(4):
#     print("*" *(i+1))

#  (6)

n = 3
for i in range(3):
    print(" " * (n-i-1), end=" ")
    print("*" * (2*i+1), end=" ")
    print(" " * (n-i-1))