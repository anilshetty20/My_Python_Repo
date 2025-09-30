# Error handling is a method which is helps to overcome the stopage of the program when the error is occured and continue the program
a=input("Enter any number :")
print(f"The multiplication of {a} is :")

try:
    for i in range(1,11):
        print(f" {int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid Input please try again!")

print("End of the program")


try:
    num=int(input("Enter the number: "))
    a=[2,3]
    print(a[num])
except ValueError:                             #error If entered invalid string
    print("The Entered value is invalid")
# except IndexError as e:
#     print(e)
except IndexError:                             # error  if index is out of range
    print("The entered value is out of range")
