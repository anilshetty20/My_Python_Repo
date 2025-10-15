f=open('functions.py','r')  #open the file in read mode
#f2=open("file2.txt","w")    #this helps in the craetion of the file which does not exists
text=f.read()   #read the entire content into the text
print(text)     #print the contents of the file
f.close()