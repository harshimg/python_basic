mylist =[1,2,3,4,5,6,7,8,9,10]
"""
for num in mylist:
    print(num)
    
for num in mylist:
    print("hello")
    
#for even no.

for num in mylist:
    if num%2==0:
        print(f"even : {num}")
    else:
        print(f"odd : {num}")
"""      
count=0

for num in mylist:
    count=count+num
print(count)

for letter in "hello world":
    print(letter)

for _ in "hello world":
    print("cool")
    
####tuple

tup=(1,2,2)

for item in tup:
    print(item)

    
my = [(1,2,9),(3,4,10),(5,6,11),(7,8,12)]
print(len(my))

#tup hack
for list in my:
    print(list)
for a,b,c in my:
    print(a)
for a,b,c in my:
    print(a,b,c)

##dict


a={"k1":1, "k2":2, "k3":3}

for item in a:
    print(a)
for key,val in a.items():
    print(val)