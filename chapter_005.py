# Chapter -5 Dictionary & Sets

# mydict = {
#     "Fast": "In a quick manner",
#     "Udoy": "Coder",
#     "Marks":[1,2,3,4],
#     "anatherdict": {'Udoy':'Player'}
# }

# print(mydict['Fast'])
# print(mydict['Udoy'])
# mydict['Marks'] = [22, 99, 436]
# print(mydict['Marks'])
# print(mydict['anatherdict']['Udoy'])

# -----------------------------------
#       Dictionary methods
# -----------------------------------

mydict = {
    "fast": "In a quick manner",
    "udoy": "Coder",
    "marks":[1,2,3,4],
    "anatherdict": {'Udoy':'Player'}
}

# print(mydict.keys())
# print(list(mydict.keys()))
# print(mydict.values())
# print(type(mydict.items()))

# updatedict = {
#     "udoy": "Rice",
#     "Harry": "Banana",
#     "Maryam": "Apple"
# }
# print(mydict)
# mydict.update(updatedict) # Update the dictionary by adding key-value pairs from updatedict
# print(mydict)


# print(mydict.get('udoy2')) # returns none as udoy2 is not peresent in the dictionary
# print(mydict['udoy2']) # throws an error as udoy2 is not present in the dictionary

# ---------------------------
#       sets in python
# ---------------------------

a = {1, 2, 3, 5, 1}
# print(a)
# print(type(a))
# print(a)

#       this syntax will creat an empty dictionary and not an empty set
x = {}
# print(type(x))

#       an empty set can be creating using the below syntax

y = set()
# print(type(y))

#       adding values to an empty set
y.add(4)
y.add(5)
y.add(7)
y.add(4)
# y.add({4:5}) # cannot add list or dict to sets
# print(y)

# set method

# print(len(y))
# y.remove(4)
# print(y)

# print(y.pop())
# y.clear()
# print(y)
# print(y.union())
# print(y.intersection())