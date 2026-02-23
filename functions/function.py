def x():
    print("konichiwa")
    print("sayonara")
print(x())

def x(name):
    print(f"hello {name}")
print(x("void"))

def x(name="default"):
    print(f"hello {name}")
print(x())

def y(num1,num2):
    return num1+num2
result = y(3,4)
print(result)

####
def print_res(a,b):
    print(a+b)
    
def return_res(a,b):
    return a+b

print(print_res(10,20)) #nonetype , u cannot assign variable 
aa=print(print_res(10,20))
print(type(aa))


print(return_res(10,20))
bb=print(return_res(10,20))
print(type(bb))

def sum_number(num1,num2):
    return num1 + num2
res=sum_number("10","30")
print(res)
