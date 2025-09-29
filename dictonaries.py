#Dictionay is a key value pair and we can access the values by using the key and vice versa
# These are ordered
dict = {
    "name" : "anil",
    "age"  : 24,
    "city": "Udupi"
}
print(dict)
print(type(dict))
print(dict["name"])  # access the data items
print(dict.get("age"))  #another way of access the dict items
print(dict.keys())    # it will print all the keys
print(dict.values())  # it will print all the values

# iterate using for loop to print the keys
for key in dict.keys():
    print(key)            #this prints keys
    print(dict[key])      #this prints the values

#iterate the for looop to print the loops
for val in dict.values():
    print(val)
print("\n")

#this for loops helpss to print both the key and value 
for key,val in dict.items():   #items which gets the both key and value
    print(key,val)