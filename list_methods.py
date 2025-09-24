l=[33,44,1,2,3,4,5,6,7,4,4,2,5]
l.append(10) #add the ele at the end of the list
print(l)
l.sort()  #sort the ele in ascending order
print(l) 
#l.sort(reverse=True)  #sort the elements in desc order
print(l)
print(l.index(10)) #gives the position of element at which index position for the ele with first occurence only
print(l.count(4))  #gives of count of the ele how many times occured
l.insert(4,899)    #this method helps to insert the ele at the specified index position in the list
print(l)

#copy the elements to other
a=[1,2,3,4]
c=["hello","anil"]
b=a.copy()  #copy the ele in list to the other list
print(b)

#extend method helps in the combining the both the list like concating
a.extend(c)
print(a)
# print(a+c) # this also helps in concating the stirng