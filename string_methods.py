#strings are immutable
a="shetty@@@@@anil@@@@@@@@"
print(len(a)) #prints length of a
print(a.upper())  #converts the string a in uppercaase
print(a.lower())  # converts a to lower case
print(a.rstrip("@"))  # removes only the "@" from the rare end
print(a.replace("anil","shetty"))   #replaces anil with shetty
print(a.capitalize()) # captial the first letter of the word in the sentence and propers the sentenvce
print(a.split("shetty"))   #splits the words based on the paramaters
print(a.count("shetty"))   #conts how many times the word has appreaded in the sentence

b="Welcome to the pyhton learning, and enjoy coding"
print(b.endswith("coding")) #if the condition is true it returns True

#endswith using slicing
print(b.endswith("to", 3, 5)) # here it checks the condtion that if the word "to" comes in the specified range then it returns true or else false
print(b.find("to"))   #it retuens the index position where the first occurnece of the word if the word is not in the string then it returns -1
#print(b.index("too")) there is function called index() which raises error if the mention word is not  found in the string

print(b.isalnum()) #checks strings as alpha numeric or not like A-Z, a-z , 0-9 if space then it is not alphanumeric 
print(a.isalpha()) #only A-Z, a-z 

c="shetty"
print(c.islower()) # returns true if lowercase
print(c.isspace()) # returns true if there is only spaces if words then false

# Other methods
#startswith()
#istitle() 
#swapcase()---> converts lower to upper and upper to lower 