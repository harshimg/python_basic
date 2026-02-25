def myfunc(*args): 
    return sum(args)*0.05

print(myfunc(40,60,100,100))

def myfunc(*args):
    for item in args:
        print(item)

print(myfunc(40,60,100,200))
