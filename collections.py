#collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, OrderedDict, defaultdict, deque
a = "aaasdf jkl;"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter)
print(my_counter.most_common(1)[0][0])
#prints the letter a with the number of a\'s in the string
#first zero is the tuple
#second zero is the element
print(list(my_counter.elements()))
#prints a list of the elements

from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
#creates an orderd x, y pair
print(pt.x,pt.y)
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 1
ordered_dict['c'] = 1
ordered_dict['d'] = 1
print(ordered_dict)
#prints pairs in order of the list

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d)
#d['key']
print(d['c'])
#returns default value: 0

d = defaultdict(float)
print(d['c'])
d = defaultdict(list)
print(d['c'])

from collections import deque
d = deque()
d.append(1)
d.append(2)

d.appendleft(3)
print(d)
#appends items

d.pop()
print(d)

d.popleft(3)
#removes items on left

d.appendleft(3)
print(d)

d.extend([4,5,6])
print(d)

d.extendleft([4,5,6])
print(d)

d.rotate(2)
print(d)
#rotates 2 elements to right

d.rotate(-1)
print(d)
#rotates 1 element to the left

