'''AUTHOR:Diya Krishna
Date:1/12/2024'''
import random
dice=input("you can start rolling a die by entering 'start' OR end the game by entering 'end' ? :")
if dice=="start":
	def roll_dice():
		return random.randint(1, 6)
	result=roll_dice()
	print("The result of dice rolled is ",result)
	print("Thankyou for playing")
else:
	print("Thankyou for playing the game!")