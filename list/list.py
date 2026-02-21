list1 =[1,2,3]
list1=['string',10,21.1]
list1=["one","two","three"]

print(list1[0]) #indexing
print(len(list1)) 

print(list1[1:3]) #slicing

list2=["four","five"]

a= list1+list2
print(a) #concatinate

a[0]="zero" # uptate or change element of list
print(a)

a.append("six") #add new item at the end
print(a)

#a.pop() #remove last element
print(a)
popped_item = a.pop(0) #pop specific index
print(popped_item)
print(a)

b=['a','c','e','d','b']
c=[9,3,2,4,5]

sorted1=b.sort()
print(sorted1) #return none
sorted2=c.sort()
print(sorted2) #return none

b.sort()
sorted1=b
print(sorted1) #or print(b)

c.reverse()
print(c)
