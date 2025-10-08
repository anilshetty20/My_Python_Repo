#Enumerate is a built in function that is used to loop over a sequence 
num=["anil",2,"car",4,"rich",6]
for index,n in enumerate(num):  #this takes both the value of the index and the num values 
    print(n)
    if(index==3):
        print("Anil is a good boy")