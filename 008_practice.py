# -------------------------------------
# Chapter -8 practice set...
# -------------------------------------

#  (1)

def maximun(num1, num2, num3):
    if (num1>num2):
        if (num1>num3):
            return num1
        else:
            return num3
    else:
        if (num2>num3):
            return num2
        else:
            return num3

m = maximun(13, 5, 2)
# print("The value of the maximum is " + str(m))

#  (2)

def farh(cel):
    return (cel *(9/5)) + 32

c = 0
f = farh(c)
# print("Fahreheit Temperature is " + str(f))

#  (3)

# print("Hello", end=" ")
# print("How", end=" ")
# print("are", end=" ")
# print("You", end=" ")

#  (4)

def recursion(n):
    if (n==1 or n==0):
        return 1
    return n * recursion(n-1)

f = recursion(5)
# print(f)

#  (5)

# n = 6
# for i in range(n):
#     print("*" * (n-i)) # prints * n-i times

#  (6)
def remove_and_split(string, word):
    newStr = string.replace(word, " ")
    return newStr.strip()

this = "          Udoy is a good           "
n = remove_and_split(this, "Udoy")
# print(n)


# this = "          Udoy is a good           "
# print(this)
# print(this.strip())

#  (7)

num = int(input("Enter the number: "))
for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")