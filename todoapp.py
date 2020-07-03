"""A to-do app using Python's tkinter

Usage:
    Type in the text field and press enter/return key to add a to-do
    Click on "Done" to disable the to-do
    Click on ❌ to delete a to-do

Note:
    1) The maximum number of characters one can input is 70

    2) Empty to-dos will not be added to the list

    3) Clicking the "Done" button will not delete the to-do.
    It will merely disable it
    To delete a to-do, use the ❌ button

Author:
    King Phyte

Email:
    kofiasante1400@gmail.com

Version:
    0.0.7
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Todo:
    """
    The main app
    """
    i = 1

    def __init__(self):
        """Initializer"""
        self.root = tk.Tk()
        self.root.title("To-Do")
        self.root.geometry("600x600")
        self.default_frame = ttk.Frame(self.root, width=400, height=400)
        self.default_frame.pack()
        self.new_todo()
        self.root.mainloop()

    def new_todo(self):
        """Creates new to-do app"""
        text_entry_field = ttk.Entry(self.default_frame, width=98)
        text_entry_field.grid(columnspan=20)
        text_entry_field.focus()

        text_entry_field.bind("<Return>",
                              lambda e: self.add_todo(text_entry_field))

    def add_todo(self, widget):
        """Adds a to-do label"""
        user_text = widget.get()

        todos = []
        rows = []

        def done_handler():
            """Disables a to-do"""
            try:
                if to_do.state()[0] == "disabled":
                    to_do.configure(state="normal")
                    cross_out.configure(text="Done")

            except Exception:
                to_do.configure(state="disabled")
                cross_out.configure(text="Not Done")

        def delete_todo_handler():
            """Deletes a to-do"""
            try:
                if to_do in todos:
                    if todos in rows:
                        for i in todos:
                            i.destroy()
            except Exception:
                print(Exception)

        if user_text != "" and len(user_text) <= 70:
            to_do = ttk.Label(self.default_frame, text=user_text)
            to_do.grid(row=Todo.i, columnspan=16, column=1, sticky="ew")

            cross_out = ttk.Button(self.default_frame, text="Done",
                                   command=done_handler)
            cross_out.grid(row=Todo.i, column=0, sticky="ew")

            delete_todo = ttk.Button(
                self.default_frame, text="❌",
                command=delete_todo_handler)
            delete_todo.grid(row=Todo.i, column=19, sticky="we")
            widget.delete("0", "end")
            widget.focus()
            todos.append(to_do)
            todos.append(cross_out)
            todos.append(delete_todo)

            rows.append(todos)
            Todo.i += 1

        elif len(user_text) > 70:
            messagebox.showinfo(title="To-Do App",
                                message="Maximum characters allowed is 70")


def main():
    """
    Runs the application
    """
    Todo()


if __name__ == "__main__":
    main()
