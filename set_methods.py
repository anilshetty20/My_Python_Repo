s1={1,2,3,4}
s2={3,4,5}
print(s1.union(s2)) #combine both s1 and s2 using union method and here its does not print repetations
print(s1.intersection(s2))  # prints only the values which is present in both s1 and s2
s1.update(s2)    # this method updates the s1 like takes the values of the s2 
print(s1,s2)

#the difference() and difference_update() method only prints the values which is present in the original set and not in both the sets
print(s1.symmetric_difference(s2)) # prints the data items which is not common in both the sets
print(s1.difference(s2))
print(s1.difference_update(s2))
s3={1,2}
print(s3.issubset(s1))  #checks wheter the items in s3 is present in s1 if yes then it prints True
print(s1.issuperset(s3))  #checks wheather its a super set of s3 if yes prints true
s3.add(33)    #add the element to the set
print(s3) 
print(s1.discard(4))   #remove/discard removes the data items in the 
print(s1.pop())     #removes the items from the sets but dont know which is deleted becoz sets are unordered