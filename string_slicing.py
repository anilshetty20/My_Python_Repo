fruits="mango"
length=len(fruits)
print("The length of word mango is",length)
print(fruits[0:5])  #to print whole word
print(fruits[:5]) #this also prints the whole word
print(fruits[:])  #this also prints the whole word
print(fruits[0:])  #this also prints the whole word
print(fruits[1:4])  #this printsthe 1 word to 4 word
#negative indexing slicing
print(fruits[0:-2])  
print(fruits[-4:-2]) #this is valid becaused length of fruits is 5-4 =1 and 5-2=3 so slicing from 1 to 3 is valid. if it is -2 to -4 is not valid that is  3 to 1 is not valid
print(fruits[-2:-4]) # this does not print anything as it is not valid