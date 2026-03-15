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