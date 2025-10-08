import random
import string
str=input("Enter the string : ")
words=str.split(" ")
coding=input("Enter 1 for coding and 0 for decoding: ")
coding=True if coding=="1" else False #This is to encrty the mssg
print(coding)
#coding = False  #This to decrypt the mssg if want to derypt comment the above line and uncomment this line of code
if(coding):
    nword=[]
    for word in words:
     if(len(word)>=3):
        r1 = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
        r2 = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
        stword=r1+ word[1:]+word[0] +r2
        nword.append(stword)
     else:
        nword.append(word[::-1])
    print(" ".join(nword))

else:
    nword=[]
    for word in words:
     if(len(word)>=3):
        stword=word[3:-3]
        stword=stword[-1]+stword[:-1]
        nword.append(stword)
     else:
        nword.append(word[::-1])
    print(" ".join(nword))
   


