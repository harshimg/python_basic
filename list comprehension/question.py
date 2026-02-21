#2

num =[x for x in range(1,50) if x%3==0]
print(num)

#3
st="print every word in this sentence that has an even number of letters"

for word in st.split():
    if len(word)%2==0:
        print(word+ " is even!")
    
    
# if len(st)%2==0:
#     print("even!")
# else:
#     print("odd")

