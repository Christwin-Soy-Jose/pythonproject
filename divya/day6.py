'''Author:Divya Kuriakose
Date:17-12-2024
program to get phone number and insert into list
'''
phone_numbers=[]
n = int(input("Enter how many phone numbers do you want? "))
for i in range(n):
    phone_number = input(f"Enter phone number {i + 1}:")
    phone_numbers.append(phone_number)
print("Phone numbers entered:")
for number in phone_numbers:
   print(number)
