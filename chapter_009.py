# Chapter -9 File I/O

#       Use open function to read the content of a file!
# f = open('that.txt', 'r')
# f = open('that.txt') # by default the mode is r
# f = open('that.txt', 'rb') # will open for read in binary mode
# f = open('that.txt', 'w')
# f = open('that.txt', 'a')

# data = f.read()
# data = f.read(5) # reads first 5 characters from the file

# data = f.read()
# data = f.readline()
# data = f.readline()
# data = f.readline()

# f.write("Please write this to the file hey")
# f.write(" Im appending")
# print(data)

# f.close()

#----------------------------------

with open('that.txt', 'r') as f:
    # a = f.read()
    # a = f.readable()
    # a = f.readline()
    # a = f.readlines()
print(a)