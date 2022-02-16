#tuples: ordered, unchangeable, allows duplication of elements
thisTuple = ("Dan", 18, "Orlando")
print(thisTuple)

myTuple = ("Jimmy",)
print(myTuple)

someTuple = tuple(["Dan",18,"Orlandy"])
someItem = thisTuple[-2]
a_tuple = ('b','a','n','a','n','a')
print(someTuple.index('n'))
print(len(someTuple))

a_list = list(a_tuple)
print(a_list)

a = (1,2,3,4,5,6,7,8,9,10)

b = a[2:5]
c = a[::-1]
d = a[::]

some_tuple = (0,1,2,3,4)
i1, *i2, i3 = some_tuple

print(i1)
print(i3)
print(i2)

import sys

d_list = [0,1,2,"hi",True]
d_tuple = (0,1,2,"hi",True)
print(sys.getsizeof(d_list),"bytesizes")
print(sys.getsizeof(d_tuple),"bytesizes")

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=100000))