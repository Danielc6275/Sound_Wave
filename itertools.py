# most common iterator is the list
#itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product, permutations, combinations, combinations_with_replacement,accumulate, groupby
import operator
a = [1,2]
b = [3,5]
prod = product(a,b, repeat=2)
#print(list(prod))

#Permutations: moving the nums around
a = [1,2,3]
perm = permutations(a)
print(list(perm))

#Combinations: returns all possible combos with a specified length
a = [1,2,3,4]
comb = combinations_with_replacement(a,2) # combinations(var, length)
print(list(comb))

#Accumulation:
a = [1,2,3,4,5]
acc = accumulate(a, func=operator.mul) #Func keyword used as a 2nd arg
print(a)
print(list(acc))

#Groupby: makes iterator that returns keys and groups
def less_than_3(x):
    return x < 3
a = [1,2,3,4]
group_obby = groupby(a, key=less_than_3)
for key, value in group_obby:
    print(key,list(value))