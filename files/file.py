"""myfile=open('files/myfile.txt')
print(myfile.read())
#myfile.close()
myfile.seek(0)
print(myfile.read())
print(myfile.read())
myfile.seek(0)

content=myfile.read()
print(content)
myfile.seek(0)

print(myfile.readlines())

myfile.close() """

####

with open("files/myfile.txt") as my_new_file:
    content=my_new_file.read()
    
print(content)


with open("files/myfile.txt",mode='r') as my_new_file: 
    content=my_new_file.read()
my_new_file.close()
#mode ="r"-> read the file|| w->write ||a->append( any more line to the end)
#r+ -> read and write
#w+ -> write and read
print(content)

######### mode-a

with open('files/my_new_file.txt',mode="r") as f:
    print(f.read())
    
with open("files/my_new_file.txt",mode="a") as f:
    print(f.write("\n4 on four"))
    
with open('files/my_new_file.txt',mode="r") as f:
    print(f.read())
    
######## mode-w

with open("files/asdfgh.txt",mode="w") as g:
    g.write("i am the owner")
    
with open("files/asdfgh.txt",) as g:
    print(g.read())