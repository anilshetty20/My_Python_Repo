# Recursion for the Factorial of a number
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

print("The Factorial of a number is :",fact(5))