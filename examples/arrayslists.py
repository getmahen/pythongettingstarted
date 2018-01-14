#ARRAYS/LISTS
nameToAdd = "Mahi"
names = ["John", "Doe"]

if nameToAdd in names == True:
    print('Found him')
else:
    names.append(nameToAdd)

print("Length of the list after addition: {0}".format(len(names)))

#delete "Mahi" from the list/array
del names[names.index(nameToAdd)]

print("Length of the list after deletion: {0}".format(len(names)))