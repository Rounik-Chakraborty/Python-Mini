import tkinter as tk
from tkinter import messagebox

# Function to update the entry widget when a button is pressed
def button_click(item):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(item))

# Function to clear the entry widget
def button_clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression and display the result
def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Creating the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")

# Creating the entry widget for displaying expressions and results
entry = tk.Entry(window, width=20, font=('Arial', 24), borderwidth=2, relief='solid')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Defining the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_value = 1
col_value = 0

# Adding buttons to the window
for button in buttons:
    if button == "=":
        btn = tk.Button(window, text=button, width=10, height=3, command=button_equal)
    else:
        btn = tk.Button(window, text=button, width=10, height=3, command=lambda b=button: button_click(b))
    btn.grid(row=row_value, column=col_value, padx=5, pady=5)
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

# Adding the Clear button
btn_clear = tk.Button(window, text='C', width=10, height=3, command=button_clear)
btn_clear.grid(row=row_value, column=col_value, padx=5, pady=5)

# Running the main loop
window.mainloop()
