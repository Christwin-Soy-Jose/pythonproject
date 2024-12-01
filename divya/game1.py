'''
Author:Divya Kuriakose
Date:1-12-2024

'''

import random
choices=["rock","paper","scissors"]
user_score=0
computer_score=0
while True:
    user_choice=input("Select rock,paper,scissors or quit: ")
    if user_choice == quit:
      print("The game is over")
      break
    elif user_choice not in choices:
        print("Invalid choice, Try again")
        continue

    computer_choice=random.choice(choices)
    print(f"Computer choose:{computer_choice}")
    if user_choice==computer_choice:
        print("Its a tie")
    elif (user_choice=="rock" and computer_choice=="scissors") or \
        (user_choice=="paper" and computer_choice=="rock") or \
            (user_choice=="scissors" and computer_choice=="paper"):
        print("You win")
        user_score +=1
    else:
        print("Computer wins")
        computer_score +=1

    print("\nFinal score")
    print(f"You: {user_score} and Computer: {computer_score}")

    if user_score> computer_score:
        print("Congratulations...You win!! ")
    elif(user_score< computer_score):
        print("Computer wins")
    else:
        print("Its a tie!!!")

