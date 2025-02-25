file_name_c="A.txt"
file_name_p="B.txt"
with open(file_name_c, 'r') as file:
    content=file.read()
with open(file_name_p,'w') as file:
    file.write(content)

