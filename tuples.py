# Tuples are ordered collection of data items. These are unchangable means cannt be changed once cretaed
tup=(1,2,3,"hello","anil",468,283)
print(type(tup))
# tup[0]=90  #this give error as we cannot modify the tuple if we try to insert the ele inside tuple it will give the error

tup2=tup[1:4] #this is slicing in tuple which gives the new tuple 
print(tup2)