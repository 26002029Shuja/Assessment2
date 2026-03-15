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