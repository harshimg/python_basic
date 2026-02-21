my_dict={'key1':"value1",'key2':"value2"}
print(my_dict)

print(my_dict['key1'])

cost = {'apple':30,"berry":10}
print(cost['apple'])

a={'k1':['a','b','c'],'k2':[1,2,3],'k3':{'insideKey':222}}
print(a['k2'])
print(a['k2'][1])
print(a['k3']['insideKey'])

myList=a["k1"]
print(myList)
letter=myList[2]
print(letter.upper())

print(a["k1"][2].upper())

b={"k1":10,"k2":20}
b["k3"]=30
b["k2"]="bye ye"
print(b)

print(b.keys())
print(b.values())
print(b.items())