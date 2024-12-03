'''
Author : Ellen Joy
guessing game
'''

import random

n = random.randrange(1, 10)
print("Welcome to the guessing game!")
guess = int(input("Enter any number:"))
while n != guess:
    if guess > n:
        print("Too high")
        guess = int(input("Enter a number again "))
    elif guess < n:
        print("Too low")
        guess = int(input("Enter a number again "))
print("You guessed it right!")
