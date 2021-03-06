#Lambda function: expression
from functools import reduce
add10 = lambda x: x + 10
print(add10(5)) #Similar to a normal function
#add10(x)
def add10_func(x):
    return x + 10

mult = lambda x,y: x*y
print(mult(2,5))

points2D = [(1, 2), (15,1),(-5,1),(4,11)]
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1]) #returns the array in the order of least to greatest of the sums

print(points2D)
print(points2D_sorted)

#map(func,sequence)
a = [1,2,3,4,5]
b = map(lambda x: x*2,a)
print(list(b))

c = [x*2 for x in a]
print(c)

#filter(func,seq)

b = filter(lambda x: x*2,a)
print(list(b))

c = [x for x in a if x%2==0]
print(c) #Important

#reduce(func,seq)
product_a = reduce(lambda x,y: x*y, a)
print(product_a)