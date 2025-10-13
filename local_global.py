#Local variable is the variable within the function and accessible within the function only
#Global variable which is declared outside of the function and it can also be accessed within the function

x=10 # this is the global variable

def hello():
    global x  # this will override the x=10 and assign x=5 as the global variable
    x=5
    y=20     # this is the local variable
    print(y)

hello()
print(x)
#print(y)   #this is trying to print the local variable outside the function which will throw the error