n=int(input("Enter how many times you want to try giving the inputs: "))
for x in range(n):
    a=int(input("Enter the number: "))
    if a < 0:        
        print("The entered number is negative so again enter the number")
        continue
    if a==0:
        print("The entered number is 0 so break the loop")
        break
    else:
        print("The entered number is postive that is =", a)