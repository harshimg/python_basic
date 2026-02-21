string1="hello"
list1=[]
for letter in string1:
    list1.append(letter)   
print(list1)

list1=[letter for letter in string1]
print(list1)

list2=[xyy for xyy in "word"]
print(list2)

list3=[num**3 for num in range(0,9)]
print(list3)

list4=[num**2 for num in range(0,10) if num%2==0]
print(list4)

celcius=[0,10,20,34.5]
fahrenheit=[((9/5)*temp +32) for temp in celcius]
print(fahrenheit)

##same as up ceelcius to fahren

celcius=[0,10,20,34.5]
fahrenheit=[]
for temp in celcius:
    fahrenheit.append((9/5)*temp +32)
print(fahrenheit)
