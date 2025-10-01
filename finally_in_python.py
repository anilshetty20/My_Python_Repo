# Finally is a keyword which is always execuated irresppective of the try and except
try:
    l=[1,2,3,4,5,6]
    i=int(input("Enter the index number :"))
    print(l[i])
except:
    print("some error oocured !")

finally:
    print("This will print irrecpective of the try and except")
    