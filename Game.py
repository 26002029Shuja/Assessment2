import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("Welcome to Rock Paper Scissors")

while True:

    user = input("Enter rock, paper, scissors or quit: ").lower()

    if user == "quit":
        break

    if user not in choices:
        print("Invalid choice")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)


if user == computer:
        print("Tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print("Score -> You:", user_score, "Computer:", computer_score)