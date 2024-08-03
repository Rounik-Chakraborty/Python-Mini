import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        # Initialize the board and current player
        self.current_player = "X"
        self.board = [""] * 9
        
        # Create buttons for the game board
        self.buttons = [tk.Button(root, text="", font=("Arial", 24), width=5, height=2, command=lambda i=i: self.button_click(i))
                        for i in range(9)]
        
        # Create the layout
        for i in range(3):
            for j in range(3):
                self.buttons[i*3 + j].grid(row=i, column=j)
        
    def button_click(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
            elif all(self.board):
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != "":
                return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
