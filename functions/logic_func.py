def even_check(num):
    return num%2==0
print(even_check(10))

# return true if no is even inside list

def check_even_list(num_list):
    for num in num_list :
        if num%2==0:
            return True
        else:
            pass
    return False    
print(check_even_list([1,1,5]))

# return all even inside list

def check_even_list(num_list):
    a=[]
    for num in num_list :
        if num%2==0:
            a.append(num)
        else:
            pass
          
    return a

print(check_even_list([2,4,5,9,33,8]))
print(check_even_list([1,9,33,99]))
        