ep1={111:10,222:20, 333:30}
ep2={444:44,555:55}
ep1.update(ep2)  #combines both
print(ep1)
# ep1.clear()   #empties the dictinory
# print(ep1)
ep1.pop(111)    #delets the firt key
print(ep1)
del ep1[444]    # this also del the key from the dict with del keyword
print(ep1)  # removes the key 444 and prints other items
