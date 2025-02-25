import os 
path=os.getcwd()
contents=os.listdir(path)
for element in contents:
    if os.path.isdir(element):
        print(element)