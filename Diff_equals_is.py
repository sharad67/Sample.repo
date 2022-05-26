# difference between using "==" and the "is" keyword when doing comparisons.
# The difference between these is that "==" checks to see if values are equal, and
# the "is" keyword checks their identity, which means it's going to check if the values are identical in terms of being the same object in memory.
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
if list1 == list2:
    print(True)
else:
    print(False)

if list1 is list2:
    print(True)
else:
    print(False)

list3 = [1, 2, 3, 4, 5]
list4 = [1, 2, 4, 5]
if list3 == list4:
    print(True)
else:
    print(False)

list5 = [1, 2, 3, 4, 5]
list6 = list5
if list5 is list6:
    print(True)
else:
    print(False)

list5[4] = 50
print(list5)
print(list6)

print(id(list3))
print(id(list4))
print(id(list3)==id(list4))
print(id(list5) == id(list6))
print(id(list5))
print(id(list6))
