'''
Author:Divya Kuriakose
Date:1-12-2024
Program to check whether a number is armstrong or not
'''

number=int(input("enter a number"))
value=number
sum=0
while(value>0):
    r=value % 10
    sum+=r **3
    value//=10

if(number==sum):
    print(number,"is a Armstrong number")
else:
    print(number,"is not a Armstrong number")
