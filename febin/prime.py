num=int(input("Enter your number :"))
for i in range (2,(num//2)+1):
    if (num%i)==0:
        print(f"The number {num} is not a prime number")
        break
else:
    print(f"The number {num} is a prime number")