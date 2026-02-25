# **kwargs return dictionary

def myfunc(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        #print(f"my fruit of choice is {kwargs}")
        print("my fruit of choice is {}".format(kwargs["fruit"]))
    else:
        print("i did not find any fruit")
print(myfunc(fruit="apple",veg="lettuce"))