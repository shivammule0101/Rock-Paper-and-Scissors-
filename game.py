import tkinter as tk
from random import randint
from time import sleep

options = ["R", "P", "S"]

LOSS_MESSAGE = "You lost!"
WIN_MESSAGE = "You won!"

def decide_winner(user_choice, computer_choice):
    user_choice_index = options.index(user_choice)
    computer_choice_index = options.index(computer_choice)
    if user_choice_index == computer_choice_index:
        return "It's a tie!"
    elif (user_choice_index == 0 and computer_choice_index == 2) or (user_choice_index == 1 and computer_choice_index == 0) or (user_choice_index == 2 and computer_choice_index == 1):
        return WIN_MESSAGE
    else:
        return LOSS_MESSAGE
def play_RPS(user_choice):
    computer_choice = options[randint(0, len(options)-1)]
    result = decide_winner(user_choice, computer_choice)
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")

#creating main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create buttons for Rock, Paper, and Scissors
rock_button = tk.Button(root, text="Rock", width=20, command=lambda: play_RPS("R"))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", width=20, command=lambda: play_RPS("P"))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", width=20, command=lambda: play_RPS("S"))
scissors_button.pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="Choose Rock, Paper, or Scissors!", width=40, height=4)
result_label.pack(pady=20)

# Start the GUI loop
root.mainloop()
