import os 
# os.mkdir("Data") #this helps in the creation of the folder called data
for i in range(0,5):
   # os.mkdir(f"Data/folder{i+1}") #This creater five folders inside the folder called Data
    os.rename(f"Data/folder{i+1}",f"Data/toturial{i+1}")  #This renames the name of the fodler

