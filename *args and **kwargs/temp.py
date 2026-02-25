def myfunc(*args):
    res=[]
    for num in args:
        if num %2==0:
            res.append(num)
    return res
print(myfunc(2,3,5,6))

def myfunc(*args):
    res = " "
    for string in args:
        if string%2==0:
            print("dd")           
##### ch           
def myfunc(mystring):
    result = ""
    
    for i, char in enumerate(mystring):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    
    return result


def myfunc(mystring):
    result = ""
    
    for i in range(len(mystring)):
        if i % 2 == 0:
            result += mystring[i].upper()
        else:
            result += mystring[i].lower()
    
    return result
## myy
def myfunc(string):
    res = ""
    
    for i in range(len(string)):
        if i%2==0:
            res += string[i].upper()
        else:
            res+= string[i].lower()
    return res

print(myfunc("hello"))