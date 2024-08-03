import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("400x300")
        self.current_question = 0
        self.score = 0
        
        # Questions and answers
        self.questions = [
            {"question": "What is the capital of France?", "answers": ["Paris", "London", "Rome", "Berlin"], "correct": "Paris"},
            {"question": "What is the largest planet in our solar system?", "answers": ["Earth", "Mars", "Jupiter", "Saturn"], "correct": "Jupiter"},
            {"question": "Who wrote 'To Kill a Mockingbird'?", "answers": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"], "correct": "Harper Lee"}
        ]
        
        # Create widgets
        self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=350)
        self.question_label.pack(pady=20)

        self.answer_buttons = [
            tk.Button(root, text="", font=("Arial", 12), width=20, command=lambda i=i: self.check_answer(i))
            for i in range(4)
        ]
        for button in self.answer_buttons:
            button.pack(pady=5)
        
        self.next_button = tk.Button(root, text="Next", font=("Arial", 12), command=self.next_question)
        self.next_button.pack(pady=20)

        self.show_question()

    def show_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text=question["question"])
        for i, answer in enumerate(question["answers"]):
            self.answer_buttons[i].config(text=answer, state=tk.NORMAL)

    def check_answer(self, index):
        question = self.questions[self.current_question]
        if self.answer_buttons[index].cget("text") == question["correct"]:
            self.score += 1
            messagebox.showinfo("Correct!", "That's the right answer!")
        else:
            messagebox.showinfo("Incorrect", "Sorry, that's not correct.")
        for button in self.answer_buttons:
            button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
            self.next_button.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("Quiz Completed", f"Your score is {self.score}/{len(self.questions)}")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
