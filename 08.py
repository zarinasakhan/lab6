import os
path=r'/Users/zarina/Desktop/kbtu/PP2/pp2/lab6/yes.py'
if os.access(path, os.F_OK):
    os.remove(path)    
else:
    print("path doesn't exist")