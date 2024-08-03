import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

# Create database and table if not exists
conn = sqlite3.connect('contacts.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        name TEXT,
        phone TEXT,
        email TEXT
    )
''')
conn.commit()
conn.close()

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x400")

        # Create a frame for the contact list
        self.contact_frame = tk.Frame(root)
        self.contact_frame.pack(pady=10)

        # Create and pack the contact listbox
        self.contact_listbox = tk.Listbox(self.contact_frame, width=50, height=15)
        self.contact_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        # Create and pack the scrollbar
        self.scrollbar = tk.Scrollbar(self.contact_frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.contact_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.contact_listbox.yview)

        # Create buttons
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)

        self.edit_button = tk.Button(root, text="Edit Contact", command=self.edit_contact)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)

        # Load contacts
        self.load_contacts()

    def load_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        c.execute('SELECT * FROM contacts')
        contacts = c.fetchall()
        for contact in contacts:
            self.contact_listbox.insert(tk.END, f"{contact[1]} - {contact[2]} - {contact[3]}")
        conn.close()

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter name:")
        phone = simpledialog.askstring("Input", "Enter phone number:")
        email = simpledialog.askstring("Input", "Enter email address:")
        if name and phone and email:
            conn = sqlite3.connect('contacts.db')
            c = conn.cursor()
            c.execute('INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)', (name, phone, email))
            conn.commit()
            conn.close()
            self.load_contacts()

    def edit_contact(self):
        selected = self.contact_listbox.curselection()
        if selected:
            index = selected[0]
            contact_id = self.get_contact_id(index)
            name = simpledialog.askstring("Input", "Enter new name:")
            phone = simpledialog.askstring("Input", "Enter new phone number:")
            email = simpledialog.askstring("Input", "Enter new email address:")
            if name and phone and email:
                conn = sqlite3.connect('contacts.db')
                c = conn.cursor()
                c.execute('UPDATE contacts SET name=?, phone=?, email=? WHERE id=?', (name, phone, email, contact_id))
                conn.commit()
                conn.close()
                self.load_contacts()
        else:
            messagebox.showwarning("Warning", "No contact selected")

    def delete_contact(self):
        selected = self.contact_listbox.curselection()
        if selected:
            index = selected[0]
            contact_id = self.get_contact_id(index)
            conn = sqlite3.connect('contacts.db')
            c = conn.cursor()
            c.execute('DELETE FROM contacts WHERE id=?', (contact_id,))
            conn.commit()
            conn.close()
            self.load_contacts()
        else:
            messagebox.showwarning("Warning", "No contact selected")

    def get_contact_id(self, index):
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        c.execute('SELECT id FROM contacts')
        ids = c.fetchall()
        conn.close()
        return ids[index][0]

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
