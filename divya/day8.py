'''
Author:Divya Kuriakose
Date:17-12-2024
program to find the sum of digits
'''
limit=int(input("Enter the limit:"))
def sum_of_digits(num):
     if num<=1:
         return num
     else:
         return num+sum_of_digits(num-1)
num=limit
if num<0:
    print("Enter a positive number")
else:
    print("The sum of first",limit,"digits is:",sum_of_digits(num))
sum_of_digits(limit)