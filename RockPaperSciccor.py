
import random

computerChoices = ["Rock","Paper","Scissor"]

userChoices = input("1. Rock \n2. Paper \n3. Scissor \nEnter one of these options:")

randomChoice = random.choice(computerChoices)

if userChoices.title() == "Rock" and randomChoice == "Paper":
    print(f"Your choice: {userChoices.title()} \nBot choice: {randomChoice}")
    print("You Loose!")
elif userChoices.title() == "Rock" and randomChoice == "Scissor":
    print(f"Your choice: {userChoices.title()} \nBot choice: {randomChoice}")
    print("You Win!")
elif userChoices.title() == "Paper" and randomChoice == "Rock":
    print(f"Your choice: {userChoices.title()} \nBot choice: {randomChoice}")
    print("You Win!")
elif userChoices.title() == "Paper" and randomChoice == "Scissor":
    print(f"Your choice: {userChoices.title()} \nBot choice: {randomChoice}")
    print("You Loose!")
elif userChoices.title() == "Scissor" and randomChoice == "Rock":
    print(f"Your choice: {userChoices.title()} \nBot choice: {randomChoice}")
    print("You Loose!")
elif userChoices.title() == "Scissor" and randomChoice == "Paper":
    print(f"Your choice: {userChoices.title()} \nBot choice: {randomChoice}")
    print("You Win!")
elif (userChoices.title() == "Rock" and randomChoice == "Rock") or (userChoices == "Scissor" and randomChoice == "Scissor") or (userChoices == "Paper" and randomChoice == "Paper"):
    print(f"Your choice: {userChoices.title()} \nBot choice: {randomChoice}")
    print("Its a Tie!")
else:
    print("Please enter one of the following options!")
