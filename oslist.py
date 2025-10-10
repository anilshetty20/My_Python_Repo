import os
folders= os.listdir("Data") # this is used to list the folders inside the Data directory
print(folders)
for folder in folders: #this helps in listing the foldes using loop
    print(folder)
    print(os.listdir(f"Data\{folder}"))  #this is used to list if there is anything inside the folder which is inside the Data directory

#There are several in OS explore 