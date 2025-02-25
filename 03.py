import os
path=os.getcwd()
contents=os.listdir(path)
if os.access(path, os.F_OK):
    directory=os.path.dirname(path)
    file=os.path.basename(path)
    print(f"directory: {directory}")
    print(f"file: {file}")
else:
    print("path doesn't exist")
    