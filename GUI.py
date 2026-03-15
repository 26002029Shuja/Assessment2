import tkinter as tk
import random
from tkinter import messagebox

choices = ["rock", "paper", "scissors"]

def play(user):
    computer = random.choice(choices)

    if user == computer:
        result = "Tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        result = "You win!"
    else:
        result = "You lose!"

    messagebox.showinfo("Result", f"Computer chose {computer}\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors")


tk.Label(root, text="Choose Rock Paper or Scissors").pack()
tk.Button(root, text="Rock", command=lambda: play("rock")).pack()
tk.Button(root, text="Paper", command=lambda: play("paper")).pack()
tk.Button(root, text="Scissors", command=lambda: play("scissors")).pack()
tk.Button(root, text="Quit", command=root.destroy).pack()

root.mainloop()