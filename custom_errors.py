a=int(input("Enter the value between 5 and 10: "))
if 5<a<10:
    raise ValueError("Enter the value between 5 and 10 otherwise it will raise error")
print(a,"is a valid input")
