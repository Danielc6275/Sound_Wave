#Errors and Exceptions
a = 5
print(a)

try:
    a = 5/0
except: 
    print('whoops :)')

try:
    a = 5/0
except Exception as e:
    print(e)
#the same as:
try:
    a=5/0
except ZeroDivisionError:
    print('THis is the division error')
    #the error becomes the arg

try: 
    a = 5/0
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
else:
    print('We/re all good :)')

class InflationError(Exception):
    pass
#defined error

def test_value(x):
    if x > 192 :
        raise InflationError('Lets go Brandon!')

try:
    test_value(200)
except InflationError as e:
    print(e)

class deflationError(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value
    
def test_value(x): 
    if x < 100:
        raise deflationError('Yay!')

try: 
    test_value(200)
except InflationError as e:
    print(e)
except deflationError as e:
    print(e.message, e.value)



