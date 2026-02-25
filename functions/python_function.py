example=[1,2,3,4,5,6,7]
from random import shuffle

shuffle(example)
print(example)

result=shuffle(example)
print(result)

def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

result=shuffle_list(example)
print(result)

mylist=[" ","o"," "]
shuffle(mylist)
print(mylist)

def player_guess():
    guess=" "
    
    while guess not in ["0","2","3"]:
        guess=input("pick a no. 0,1 or 2: ")
    return int(guess)

myindex=player_guess()
print(myindex) 

def check_guess(mylist,guess):
    if mylist[guess]=="o":
        print("coreect")
    else:
        print("wrong guess!")
        print(mylist)
        
#initial list
mylist=[" ","o"," "]
#shuffle list
mixedup_list=shuffle_list(mylist)
#user guess
guess= player_guess()
#check guess
print(check_guess(mixedup_list,guess))