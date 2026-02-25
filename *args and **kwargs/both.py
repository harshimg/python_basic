def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print("i would like {} {}".format(args[0],kwargs["food"]))
    
print(myfunc(10,20,30,fruit="apple",animal ="tiger",food="dragon")) 