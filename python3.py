#dictionaries
from this import d


dictor = {"name": "Dan","age":"18","city":"Orlando"}
print(dictor)
dictor2 = dict(name="Dan", age="18",city="Orlando")

dictor["email"] = "dc6275@gmail.com"
print(dictor)

del dictor["name"]
print(dictor)

dictor.pop("age")
print(dictor)

dictor.popitem()
print(dictor)

if "name" in dictor:
    print(dictor["name"])

try: 
    print(dictor["name"])
except:
    print("error")

for key in dictor:
    print(key)

for key,value in dictor.items():
    print(value)

dictor_cpy = dictor
print(dictor_cpy)

dictor_cpy["email"] = "dc6275@gmail.com"
print(dictor_cpy)
print(dictor)

dictor.update(dictor2)
print(dictor)

dictor = {3: 9, 6: 36, 9:81}
print(dictor)

value = dictor[3]
print(value)

tuple_dict = (8,6)
dictor = {tuple_dict: 14}

print(dictor)
