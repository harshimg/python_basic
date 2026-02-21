#### zip function ( zip 2or more list and pair up item)
## only zip upto shortes element in list and ignore extra

list1=[1,2,3,4,5]
list2=["a","b","c"]
list3=[2,4,6]

for a,b,c in zip(list1,list2,list3):
    print(a)

print(list(zip(list1,list2,list3)))