import random

choices = ["rock", "paper", "scissors"]

Player = None
Computer = random.choice(choices)

while Player not in choices:
    Player = input("your guess: ").lower()

if Player == Computer:
    print("player's choice: ", Player)
    print("computer's choice: ", Computer)
    print("it's a tie")
elif Player == "rock":
    if Computer == "paper":
        print("player's choice: ", Player)
        print("computer's choice: ", Computer)
        print("computer wins")
    if Computer == "scissors":
        print("player's choice: ", Player)
        print("computer's choice: ", Computer)
        print("Computer wins")
elif Player == "paper":
    if Computer == "scissors":
        print("player's choice: ", Player)
        print("computer's choice: ", Computer)
        print("computer wins")
    if Computer == "rock":
        print("player's choice: ", Player)
        print("computer's choice: ", Computer)
        print("player wins")
elif Player == "scissors":
    if Computer == "paper":
        print("player's choice: ", Player)
        print("computer's choice: ", Computer)
        print("player wins")
    if Computer == "rock":
        print("player's choice: ", Player)
        print("computer's choice: ", Computer)
        print("Computer wins")


