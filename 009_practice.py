# -------------------------------------
# Chapter -9 practice set...
# -------------------------------------

#  (1)


# with open('this.txt') as f:
#     x = f.read()
#     if "Twinkle" in x:
#         print("Yes this text in the file")
#     else:
#         print("OOps this text cannot in the file")

#  (2)


# def game():
#     return 44643534

# score = game()
# with open('hiscore.txt') as f:
#     hiscoreStr = f.read()
    
# if hiscoreStr=='':
#     with open('hiscore.txt', 'w') as f:
#         f.write(str(score))

# elif int(hiscoreStr)<score:
#     with open('hiscore.txt', 'w') as f:
#         f.write(str(score))


#  (3)


# for i in range(2, 21):
#     with open(f"tables{i}", 'w') as f:
#         for j in range(1, 11):
#             f.write(f"{i} X {j} = {i*j}\n")
#         # if im remove breake statment so auto make a one by one file and write a multiplaction table
#     break


#  (4) replace single workd in txt file


# with open('that.txt') as f:
#     content = f.read()

# content = content.replace("donkey", "$%@#$%^&")

# with open('that.txt', 'w') as f:
#     content = f.write(content)


#  (5) replace multupole words in txt file. 


# words = ["donkey", "kaddu", "mote"]

# with open('that.txt') as f:
#     content = f.read()

# for word in words:
#     content = content.replace(word, "$%@#$%^&")

# with open('that.txt', 'w') as f:
#     content = f.write(content)


#  (6) fine name of python in log file


# with open("log.txt") as f:
#     content = f.read()

# if 'Python' in content:
#     print("Yes Python in content")
# else:
#     print("Python is not in content")


#  (7) find line number in python in txt file


# content = True
# i = 1
# with open("log.txt") as f:

#     while content:
#         content = f.readline()
#         if 'python' in content:
#             print("Yes Python in content")
#             print(i)
#         i+=1


#  (8) copy text in this.txt to copy.txt


# with open('this.txt') as f:
#     content = f.read()

# with open('copy.txt', 'w') as f:
#     content = f.write(content)

