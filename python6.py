#strings: ordered, immutable, text representation
from timeit import default_timer as timer
string_wrap = 'WASSAP world!'
print(string_wrap)

string_wrap = 'I\'m a programmer'

string_wrap = """Wassup \
    World"""
print(string_wrap)
#used for multi-line strings and code documentation
#back slash continues string on another line
char = string_wrap[0]
print(char)
#returns first character of string

char = string_wrap[-1]
print(char)
#returns last character of string

string_wrap[0] = 'W'
print(string_wrap)
#returns error since strings are immutable

substring = string_wrap[1:5]
print(substring)
#returns index 1-4, excludes index 5 in the chars

substring = string_wrap[::1]
print(substring)
#returns every character

substring = string_wrap[::2]
print(substring)
#returns every second character

substring = string_wrap[::-1]
print(substring)
#reverses the string order

#concatenate 2 or more string
greeting = 'Hi'
name = 'Jak'
sentence = greeting + "" + name
print(sentence)

for i in greeting:
    print(i)

if 'e' in greeting: 
    print('yes')
else:
    print('nah man')

string_wrap = '        Howdy World       '
print(string_wrap)

string_wrap = string_wrap.strip()
print(string_wrap)
#removes white space

print(string_wrap.upper())
#makes string upper case
print(string_wrap.lower())
#makes string lower case
print(string_wrap.startswith('World'))
#prints a bool 

print(string_wrap.find('wd'))
#returns index of substring

print(string_wrap.count('o'))
#returns count of a certain number

print(string_wrap.replace('World','Partner'))
#replaces a word or character with another character

my_string = 'how\'s it going'
my_list = my_string.split()
print(my_list)
#returns each individual word in a list

my_string = 'how are you doing'
my_list = my_string.split(",")
print(my_list)
#splits everything separated by a comma

new_string = ''.join(my_list)
print(new_string)
#joins elements of a list back into string
#VERY IMPORTANT

my_list = 6
print(my_list)

start = timer()
mr_string = ''
for i in my_list:
    my_string += i
print(my_string)
stop = timer()
print(stop-start)
#this is bad code


start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop-start)
#cleaner code

var = "Tim"
my_string = "the variable is %s" % var
print(my_string)
#%s tells the placeholder that we have a string in the var variable

var = 3
my_string = "the variable is %d" % var
print(my_string)
#to input integers into string

var = 3.1415
my_string = "the variable is %.2f" % var
#2 is the number of digits after decimal

var = 3.1415
var2 = 3.12345678
my_string = f"the variable is {var *2} and {var2}".format(var,var2)
print(my_string)
#multiplies number by 2

