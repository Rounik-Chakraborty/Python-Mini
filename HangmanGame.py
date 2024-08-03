import tkinter as tk
from tkinter import messagebox
import random

class Hangman:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.word_list = ["python", "hangman", "challenge", "programming", "interface"]
        self.max_attempts = 6
        self.attempts_left = self.max_attempts

        self.initialize_game()

    def initialize_game(self):
        self.word = random.choice(self.word_list)
        self.guesses = set()
        self.correct_guesses = set()

        self.word_display = tk.Label(self.root, text=self.get_display_word(), font=("Arial", 24))
        self.word_display.pack(pady=20)

        self.attempts_display = tk.Label(self.root, text=f"Attempts left: {self.attempts_left}", font=("Arial", 16))
        self.attempts_display.pack(pady=10)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()

        self.create_keyboard()
        self.update_keyboard()

    def create_keyboard(self):
        self.keyboard_buttons = {}
        for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
            button = tk.Button(self.buttons_frame, text=letter.upper(), font=("Arial", 14), width=4, height=2,
                              command=lambda l=letter: self.make_guess(l))
            button.grid(row=i // 9, column=i % 9, padx=5, pady=5)
            self.keyboard_buttons[letter] = button

    def update_keyboard(self):
        for letter, button in self.keyboard_buttons.items():
            if letter in self.guesses:
                button.config(state=tk.DISABLED)
            else:
                button.config(state=tk.NORMAL)

    def make_guess(self, letter):
        if letter in self.guesses:
            return

        self.guesses.add(letter)
        if letter in self.word:
            self.correct_guesses.add(letter)
            if self.get_display_word().replace(" ", "") == self.word:
                self.end_game(f"Congratulations! You guessed the word: {self.word}")
        else:
            self.attempts_left -= 1
            self.attempts_display.config(text=f"Attempts left: {self.attempts_left}")
            if self.attempts_left == 0:
                self.end_game(f"Game Over! The word was: {self.word}")

        self.word_display.config(text=self.get_display_word())
        self.update_keyboard()

    def get_display_word(self):
        return " ".join(letter if letter in self.correct_guesses else "_" for letter in self.word)

    def end_game(self, message):
        messagebox.showinfo("Hangman", message)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = Hangman(root)
    root.mainloop()
