import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Initialize the main application window
class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("600x400")

        # Create GUI components
        self.create_widgets()
        
        # Initialize expenses DataFrame
        self.expenses_df = pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description'])

    def create_widgets(self):
        # Title Label
        tk.Label(self.root, text="Expense Tracker", font=("Helvetica", 16)).pack(pady=10)

        # Date
        tk.Label(self.root, text="Date (YYYY-MM-DD):").pack()
        self.date_entry = tk.Entry(self.root)
        self.date_entry.pack()

        # Category
        tk.Label(self.root, text="Category:").pack()
        self.category_entry = tk.Entry(self.root)
        self.category_entry.pack()

        # Amount
        tk.Label(self.root, text="Amount:").pack()
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack()

        # Description
        tk.Label(self.root, text="Description:").pack()
        self.description_entry = tk.Entry(self.root)
        self.description_entry.pack()

        # Add Expense Button
        self.add_button = tk.Button(self.root, text="Add Expense", command=self.add_expense)
        self.add_button.pack(pady=10)

        # Show Expenses Button
        self.show_button = tk.Button(self.root, text="Show Expenses", command=self.show_expenses)
        self.show_button.pack(pady=10)

        # Save to CSV Button
        self.save_button = tk.Button(self.root, text="Save to CSV", command=self.save_to_csv)
        self.save_button.pack(pady=10)

        # Plot Expenses Button
        self.plot_button = tk.Button(self.root, text="Plot Expenses", command=self.plot_expenses)
        self.plot_button.pack(pady=10)

    def add_expense(self):
        try:
            date = self.date_entry.get()
            category = self.category_entry.get()
            amount = float(self.amount_entry.get())
            description = self.description_entry.get()

            # Validate date
            datetime.strptime(date, "%Y-%m-%d")

            # Append new expense to DataFrame
            new_expense = pd.DataFrame([[date, category, amount, description]], columns=['Date', 'Category', 'Amount', 'Description'])
            self.expenses_df = pd.concat([self.expenses_df, new_expense], ignore_index=True)

            # Clear entries
            self.date_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)

            messagebox.showinfo("Success", "Expense added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please check your entries.")

    def show_expenses(self):
        if not self.expenses_df.empty:
            top = tk.Toplevel()
            top.title("Expenses List")
            text = tk.Text(top)
            text.pack()
            text.insert(tk.END, self.expenses_df.to_string(index=False))
        else:
            messagebox.showinfo("No Data", "No expenses to show.")

    def save_to_csv(self):
        if not self.expenses_df.empty:
            self.expenses_df.to_csv("expenses.csv", index=False)
            messagebox.showinfo("Success", "Expenses saved to expenses.csv")
        else:
            messagebox.showinfo("No Data", "No expenses to save.")

    def plot_expenses(self):
        if not self.expenses_df.empty:
            category_totals = self.expenses_df.groupby('Category')['Amount'].sum()
            category_totals.plot(kind='bar')
            plt.title('Expenses by Category')
            plt.xlabel('Category')
            plt.ylabel('Total Amount')
            plt.show()
        else:
            messagebox.showinfo("No Data", "No expenses to plot.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
