import os 
path=os.getcwd()
contents=os.listdir(path)
for element in contents:
    if os.path.isfile(element):
        print(element)