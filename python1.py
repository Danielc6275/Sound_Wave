#adding some python code 
hitList = ["banana","cherry","apple"]
print(hitList)

hitList2 = [5, True, "apple banana", "cherry"]
print(hitList2)

item = hitList[1]
print(item)

if "banana" in hitList:
    print("aw yeah")
else: 
    print("nah man")

print(len(hitList))

hitList.append("lemon")
print(hitList)

hitList.insert(1, "pear")

thing = hitList.pop()
print(item)
print(hitList)

item2 = hitList.clear()
item3 = hitList.reverse()
item4 = hitList.sort()
print(item4)

new_hitList = sorted(hitList)
print(hitList)
print(new_hitList)

listo = [0] * 5
print(listo)

listo2 = [1,2,3,4,5]

new_list = listo + listo2
print(new_list)

gist = [1,2,3,4,5,6,7,8,9]

a = gist[1:5]
print(a)
