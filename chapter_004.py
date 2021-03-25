# Chapter -4 List & Tuples

#       Create a list using []
a = [1, 2, 3, 4, 56, 6]
# print(a)

#       Print the list using print () function
# print(a)

#       Access using index uding a[0], a[1], a[2]
# print(a[2])

#       Change the value of list using
a[0] = 98
# print(a)

#       We can Create a list with items of different types
c = [45, "Udoy", False, 6.9]
# print(c)

#       List slicing

friends = ["Harry", "Udoy", "Tom", "Maryam", "Fariha", 45]
# print(friends[0:4])
# print(friends[-4:])

#-------------------------
#       List methods
#-------------------------

l1 = [1, 8, 7, 21, 15, 12, 19]
l1.sort() # Sorts the list
# print(l1)

l1.reverse() # Reverse the list
# print(l1)

l1.append(45) # adds at the end of the list
l1.append(88) # adds at the end of the list
# print(l1)

l1.insert(4, 544) # Inserts 544 at indes 4
# print(l1)

l1.pop(2) # remove element at indes 2
# print(l1)

l1.remove(21) # Remove 21 from the list
# print(l1)

# -------------------
#       Tuples
# -------------------

#       Creating a tuple using ()
tp = (1, 1, 2, 3, 4)
# t1 = () # Empty tuple

t1 = (1,) # Tuple with single element
# print(t1)

#       Printing the element of  a tuple
# print(tp[0])

#       Cannot update the values of a tuple
# tp[0] = 34
# print(tp)

# -------------------------
#       Tuple method
# -------------------------

# print(tp.count(1))
# print(tp.index(3))
# print(len(tp))