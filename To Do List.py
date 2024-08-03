import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")
        
        self.tasks = []
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        
        self.task_listbox = tk.Listbox(
            self.frame, 
            width=50, 
            height=15, 
            bd=0, 
            selectbackground="#a6a6a6", 
            activestyle="none"
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)
        
        self.entry = tk.Entry(self.root, font=("Helvetica", 24))
        self.entry.pack(pady=20)
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=20)
        
        self.add_task_button = tk.Button(
            self.button_frame, 
            text="Add Task", 
            command=self.add_task
        )
        self.add_task_button.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        
        self.remove_task_button = tk.Button(
            self.button_frame, 
            text="Remove Task", 
            command=self.remove_task
        )
        self.remove_task_button.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        
        self.clear_button = tk.Button(
            self.button_frame, 
            text="Clear All", 
            command=self.clear_all
        )
        self.clear_button.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def remove_task(self):
        try:
            task = self.task_listbox.get(tk.ACTIVE)
            if task in self.tasks:
                self.tasks.remove(task)
            self.update_listbox()
        except:
            messagebox.showwarning("Warning", "You must select a task.")
    
    def clear_all(self):
        self.tasks = []
        self.update_listbox()
    
    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
