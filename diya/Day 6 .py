'''Author:Diyakrishna
version1.1'''
names_list = []
while True:
    name = input("Enter a name (or type 'exit' to stop): ")
    if name == 'exit':
        break
    else:
        names_list.append(name)
print("Names entered:", names_list)