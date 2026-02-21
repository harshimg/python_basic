#acceptt only unique value , dont repeat

myset=set()
print(myset)

myset.add(1)
print(myset)
myset.add(2)
print(myset)
myset.add(2)
print(myset)

mylist=[1,3,4,5,1,1,2,3,4,5,3]
# a=set(mylist)
print(set(mylist))