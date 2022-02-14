#tuples: ordered, unchangeable, allows duplication of elements
thisTuple = ("Dan", 18, "Orlando")
print(thisTuple)

myTuple = ("Jimmy",)
print(myTuple)

someTuple = tuple(["Dan",18,"Orlandy"])
someItem = thisTuple[-2]

if "Dan" in thisTuple:
    print("yea")
else:
    print("nah")

a_tuple = ('b','a','n','a','n','a')
print(someTuple.index('n'))
print(len(someTuple))