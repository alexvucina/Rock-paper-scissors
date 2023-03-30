import random


exit = False
user_points = 0
computer_points = 0

while not exit:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper or scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game ended")
        print("Player total score = " +str(user_points)+ " \nComputer total score = " +str(computer_points))
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("Draw")

        elif computer_input == "paper":
            print("Your input is rock")
            print("Computer input is paper")
            print("Computer won")
            computer_points += 1

        elif computer_input == "scissors":
            print("Your input is rock")
            print("Computer input is scissors")
            print("You won")
            user_points += 1

    if user_input == "paper":
        if computer_input == "rock":
            print("Your input is paper")
            print("Computer input is rock")
            print("You won")
            user_points += 1

        elif computer_input == "paper":
            print("Your input is paper")
            print("Computer input is paper")
            print("Draw")

        elif computer_input == "scissors":
            print("Your input is paper")
            print("Computer input is scissors")
            print("Computer won")
            computer_points += 1

    if user_input == "scissors":
        if computer_input == "rock":
            print("Your input is scissors")
            print("Computer input is rock")
            print("Computer won")
            computer_points += 1

        elif computer_input == "paper":
            print("Your input is scissors")
            print("Computer input is paper")
            print("You won")
            user_points += 1

        elif computer_input == "scissors":
            print("Your input is scissors")
            print("Computer input is scissors")
            print("Draw")

if user_points > computer_points:
    print ("You won the game")
elif user_points == computer_points:
    print("The game is a draw!")
else:
    print("Computer won the game")
