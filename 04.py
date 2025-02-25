file_name='ex.txt'
count=0
with open(file_name, 'r') as file:
    for line in file:
        count+=1
print(f"the number of lines: {count}")