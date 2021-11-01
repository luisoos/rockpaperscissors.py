import random

rock = 1
paper = 2
scissor = 3

print("Welcome to rock, paper, scissors. Type in your guess below. Dont write anything wrong or capitalised!")


computer = random.randint(1, 3)

human = input("Rock, paper or scissor?:")

if human == computer:
    print("You diced the same! Try again!")
else:
    if human == "rock":
        if computer == paper:
            print("Computer choose paper, maybe you win next time.")
        elif computer == scissor:
            print("Computer choose scissor, you win!")
    elif human == "paper":
        if computer == scissor:
            print("Computer choose scissor, maybe you win next time.")
        elif computer == rock:
            print("Computer choose rock, you win!")
    elif human == "scissor":
        if computer == rock:
            print("Computer choose stone, maybe you win next time.")
        elif computer == paper:
            print("Computer choose paper, you win!")
