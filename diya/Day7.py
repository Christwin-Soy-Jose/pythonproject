'''Author:Diya krishna
version 1.1
DATE:3/12/2024'''
# to find the total number of even or odd divisors of a given integer.
def divisor(n):
    x = [i for i in range(1, n + 1) if not n % i]
    y=len(x)
    return y
n=int(input("Enter a number :"))
print(divisor(n))