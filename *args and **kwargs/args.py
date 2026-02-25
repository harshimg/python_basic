# *args(args acn be any name like *spam, *hi)- but for convention we use args
# * is the main things
# - user can many parameter as they want and its treated as a tupple
# arbitrary number of arguments

def myfunc(a,b,c=0):
    return sum((a,b,c))*0.05

print(myfunc(40,60,100))

def myfunc(*args): 
    return sum(args)*0.05

print(myfunc(40,60,100,100))

def myfunc(*args):
    for item in args:
        print(item)

print(myfunc(40,60,100,200))

