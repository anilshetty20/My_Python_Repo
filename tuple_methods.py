#tuple cannot be changed or manipulated directly but it can be converted to list and do some operation and again convert back to the tuple

tup=(1,2,3,"anil","india","shetty","udupi")
print(type(tup))
print(tup)
temp=list(tup)    #convert the tuple to list
temp.append("asia") # append the ele to list
temp[3]="hello"     #replace the ele at 3 index postion
temp.pop(5)         #removes the ele at 5 index position
print(temp)         # now this is list

tup=tuple(temp)     #conver the list to tuple
print(tup)

# In tuple we can concate two tuple
tup2=("aadi","vaibhav")
final=tup+tup2
print(final)

# In tuple we can invlove methods like --->
#coount()
#index()