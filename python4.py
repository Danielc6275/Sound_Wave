#Sets: unordered, mutable, no duplicates
set1 = {1,2,3,1,2}
print(set1)

set1 = set("howdy")
print(set1)

set1 = set([1,2,3,1,2])

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)

myset.remove(3)

myset.discard(4)
myset.clear()
print(myset.pop())
print(myset)

for i in myset:
    print(i)

if 1 in myset:
    print("aw yeah!")

odd = {1,3,5,7,9}
even = {0,2,4,6,8}
primes = {2,3,5,7}

u = odd.union(even)
print(u)
#combines odds and evens

h = odd.intersection(primes)
print(h)
#prints numbers that both odd and primes variables share

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3}
setC = {7,8}

diff = setA.difference(setB)
print(diff)
#prints numbers in setA that are NOT in setB

diff = setB.symmetric_difference(setA)
print(diff)
#displays only numbers that setA and setB don't have in common

setA.update(setB)
print(setA)
#adds elements only found in setB to setA.

setA.intersection_update(setB)
print(setA)
#puts only elements found in both setA and setB into setA.

setA.difference_update(setB)
print(setA)
#removes all numbers found in both setA and setB

setA.symmetric_difference_update(setB)
print(setA)
#returns all numbers that setA and setB dont have in common.

print(setA.issubset(setB))
print(setB.issubset(setA))
#smaller set of a larger set

print(setA.issuperset(setB))
#larger set of a smaller set

print(setA.isdisjoint(setB))

setB = setA.copy()

setB.add(7)
print(setB)
print(setA)
# edited Copy and original
setB = set(setA)

a = frozenset([1,2,3,4])

a.add(2)
a.remove(1)
print(a)
#prints error since it is a frozen set






