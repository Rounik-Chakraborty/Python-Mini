import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("300x200")

        self.target_number = random.randint(1, 100)
        self.guesses_left = 10

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Guess the Number", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.instruction_label = tk.Label(self.root, text="Enter a number between 1 and 100:")
        self.instruction_label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(self.root, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack(pady=5)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if guess < 1 or guess > 100:
                raise ValueError("Guess out of range")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a number between 1 and 100.")
            return

        if guess == self.target_number:
            self.result_label.config(text="Congratulations! You guessed the number!")
            self.submit_button.config(state=tk.DISABLED)
        elif guess < self.target_number:
            self.guesses_left -= 1
            self.result_label.config(text=f"Too low! Guesses left: {self.guesses_left}")
        else:
            self.guesses_left -= 1
            self.result_label.config(text=f"Too high! Guesses left: {self.guesses_left}")

        if self.guesses_left <= 0:
            self.result_label.config(text=f"Game over! The number was {self.target_number}.")
            self.submit_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()
