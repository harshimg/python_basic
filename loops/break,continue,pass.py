x=[1,2,3]

for item in x:
    ##
    pass #do nothing

print("end script")

string ="anthony"
"""
for letter in string:
    if letter =="t":
        continue # goes to top of enclosing loop
    print(letter)
"""    
for letter in string:
    if letter == "t":
        break #break out the current closest enclosing lopp
    print(letter)
    
x = 0

while x <5:
    if x==2:
       break
    print(x)
    x=x+1