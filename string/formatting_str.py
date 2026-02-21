 #formatting string

x="Hello World"
print(f"my name is {x}")
print("my name is {}".format(x))
print("my name is {}".format("void"))
print("my name is {} {} {}".format(x,"void",'demon'))
print("my name is {2} {0} {1}".format(x,"void","demon"))
print("my name is {y1} {z1} {a1}".format(y1=x,z1="void",a1="demon"))

result=100/777
print(result)
print("my valus is {r1:10.3f}".format(r1=result)) # {value:width.precision f}