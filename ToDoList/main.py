import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_tasks():
    listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(
    frame,
    width=50,
    height=10,
    bd=0,
    font=("Courier New", 12),
    selectbackground="#a6a6a6",
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(
    root,
    font=("Courier New", 12)
)
entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(
    button_frame,
    text="Add Task",
    font=("Courier New", 12),
    command=add_task
)
add_button.pack(side=tk.LEFT)

delete_button = tk.Button(
    button_frame,
    text="Delete Task",
    font=("Courier New", 12),
    command=delete_task
)
delete_button.pack(side=tk.LEFT)

clear_button = tk.Button(
    button_frame,
    text="Clear Tasks",
    font=("Courier New", 12),
    command=clear_tasks
)
clear_button.pack(side=tk.LEFT)

root.mainloop()
