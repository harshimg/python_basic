stock = [("appl",200),("goog",400),("msft",600)]

for item in stock:
    print(item)
    
for token,price in stock:
    print(price+(0.1*price))
    
work_hours=[("annie",10),("sophia",30),("andrew",25)]

def employ_check(work_hours):
    current_max=0
    employ_of_month=""
    
    for employ,hours in work_hours:
        if hours>current_max:
            current_max=hours
            employ_of_month=employ
        else:
            pass
        
    return (employ_of_month,current_max) 

print(employ_check(work_hours))

result=employ_check(work_hours)
print(result) 

name,hours,loc=employ_check(work_hours)#here expected 3 but get only 2
print(result)
print(name)
print(hours)