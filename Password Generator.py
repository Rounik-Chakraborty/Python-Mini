import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")

        # Title Label
        self.title_label = tk.Label(root, text="Password Generator", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Length Label and Entry
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack(pady=5)
        self.length_entry = tk.Entry(root)
        self.length_entry.pack(pady=5)

        # Options for Including Characters
        self.include_uppercase = tk.BooleanVar(value=True)
        self.uppercase_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.include_uppercase)
        self.uppercase_check.pack(pady=5)

        self.include_numbers = tk.BooleanVar(value=True)
        self.numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=self.include_numbers)
        self.numbers_check.pack(pady=5)

        self.include_symbols = tk.BooleanVar(value=True)
        self.symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=self.include_symbols)
        self.symbols_check.pack(pady=5)

        # Generate Button
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=20)

        # Password Display
        self.password_display = tk.Entry(root, font=("Arial", 14), width=40)
        self.password_display.pack(pady=10)

    def generate_password(self):
        length = self.get_password_length()
        if length <= 0:
            messagebox.showerror("Error", "Please enter a valid length.")
            return

        characters = string.ascii_lowercase
        if self.include_uppercase.get():
            characters += string.ascii_uppercase
        if self.include_numbers.get():
            characters += string.digits
        if self.include_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "No character types selected.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)

    def get_password_length(self):
        try:
            length = int(self.length_entry.get())
            if length > 0:
                return length
            else:
                return 0
        except ValueError:
            return 0

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
