#Functions is a block of code that performs a specific task whenever it is called----> instead of writing many lines of code we can use the functions to reduce the code.
#Function to check whether the number is even or odd
def evenorodd(a):
    if a%2==0:
        print("The number is even")
    else:
        print("The number is odd")

#Function to for the Area of the circle
def areaofcircle(r):
    area=3.14*r*r
    print("The area of circle is =",area)

#Function to count vowels in a string
def countvowles(str):
    count=0
    for x in str:
        if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
            count=count+1
    print("The count of vowels in a string is ",count)

evenorodd(10)                     #check even or odd
areaofcircle(3)                   #check area of a circle
countvowles("anilshetty")         #count the vowels in a string
 

