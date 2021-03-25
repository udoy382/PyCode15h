# Chapter -3 Strings

# a = 34
# b = 'Udoy"s'
# b = '''Udoy"s and harry's'''
# print(a, b)
# print(type(a))
# print(type(b))

#--------------------------
#       String Slicing
#--------------------------

# name = "Harry"
# greeting = "Good Morning "

# print(type(name))
# c = greeting + name
# print(greeting + name)
# print(c)

# name = "HarryIsGood"
# print(name[4])

# name[3] = "d" #--> Does chnage  not work

# print(name[0:4])
# print(name[-4:-1])
# print(name[0::2])

#----------------------------
#       String Function
#----------------------------

# story = "once upon a time there was a youtuber named Harry who uploaded python course with notes"
# print(len(story))
# print(story.endswith("notes"))
# print(story.count("a"))
# print(story.capitalize())
# print(story.find("upon"))
# print(story.replace("Harry", "Udoy"))

#---------------------------
#       escape sequences
#----------------------------

# story = "Harry is a \\good. \nHe \tis very good"
# print(story)