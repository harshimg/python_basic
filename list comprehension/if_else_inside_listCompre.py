list4=[num**2 for num in range(0,10) if num%2==0]
print(list4)


#not good for future
result =[x if x%2==0 else "odd" for x in range(0,12)]
print(result) 

list1=[]
for x in [2,4,6]:
    for y in [10,20,30]:
        list1.append(x*y)
print(list1)

##using list comprehension

list1=[x*y for x in [2,4,6] for y in [10,20,30]]
print(list1)