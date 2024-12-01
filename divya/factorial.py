'''
Author :Divya Kuriakose
Date:1-12-2024
Program to find the factorial
'''

number=int(input("Enter a number:"))
factorial=1
for i in range (1,number+1):
    factorial=factorial * i
print("The factorial of ",number ,"is",factorial)