mylist=[1,2,3]

for num in range(3,12,2): #(start,end,jump)
    print(num)
    
print(list(range(3,12,2)))

index_count=0

for letter in "abcde":
    print("at index {} the letter is {}".format(index_count,letter))
    index_count+=1

index_count=0
word="abcde"
for letter in word:
    print(word[index_count])
    index_count+=1
    
##enumerate function (adds a counter to an iterable and returns it as an enumerate object)

word="abcde"

for items in enumerate(word):
    print(items)
    
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print("\n")


