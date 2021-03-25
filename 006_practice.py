# -------------------------------------# Chapter -6 practice set...
# -------------------------------------

#  (1)

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# num4 = int(input("Enter fourth number: "))

# if (num1>num4):
#     f1 = num1
# else:
#     f1 = num4

# if(num2>num3):
#     f2 = num2
# else:
#     f2 = num1

# if(f1>f2):
#     print(str(f1) + " is greates")

# else:
#     print(str(f2) + " is greates")

#  (2)

# sub1 = int(input("Enter first subject marks: "))
# sub2 = int(input("Enter second subject marks: "))
# sub3 = int(input("Enter third subject marks: "))

# if (sub1<33 or sub2<33 or sub3<33):
#     print("You are fail because you have less then 33% in one of the subject")
# elif(sub1+sub2+sub3)/3 <40:
#     print("you are fail due total percentage less then 40")
# else:
#     print("Congratulation! you fass the exam")

#  (3)

# text = input("Enter the text: ")

# if ("make a lot of money" in text):
#     spam = True
# elif("buy now" in text):
#     spam = True
# elif("click this" in text):
#     spam = True
# elif("subscribe this" in text):
#     spam = True
# else:
#     spam = False

# if (spam):
#     print("This text is spam")
# else:
#     print("This text is not spam")

#  (4)

# names = ["harry", "udoy", "mahi", "amy", "suha", "Maryam", "Fariha", "hala"]
# name = input("Enter the name to check: ")

# if name in names:
#     print("Your name is present in the list")
# else:
#     print("Your name is not present in the list")


#  (5)

marks = int(input("Enter the marks: "))

if marks>=90:
    gread ="Ex"
elif marks>=80:
    gread = "A"
elif marks>=70:
    gread ="B"
elif marks>=60:
    gread = "C"
elif marks>=50:
    gread ="D"
else:
    gread = "F"
print("Your gread is " + gread)