import tkinter as tk
import random

def play(choice):
    comp = random.choice(["Rock", "Paper", "Scissor"])
    result = "Tie"
    if (choice == "Rock" and comp == "Scissor") or \
       (choice == "Paper" and comp == "Rock") or \
       (choice == "Scissor" and comp == "Paper"):
        result = "You Win"
    elif choice != comp:
        result = "You Lose"
    lbl.config(text=f"Computer: {comp} | {result}")

root = tk.Tk()
root.title("RPS Game")

for c in ["Rock", "Paper", "Scissor"]:
    tk.Button(root, text=c, width=10, command=lambda x=c: play(x)).pack(pady=5)

lbl = tk.Label(root, text="", font=("Arial", 14))
lbl.pack(pady=10)

root.mainloop()
