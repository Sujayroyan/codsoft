import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = "tasks.json"

# Load existing tasks
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Add new task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append({"title": task, "completed": False})
        update_listbox()
        save_tasks()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Update listbox display
def update_listbox():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "✅" if task["completed"] else "❌"
        listbox.insert(tk.END, f"{i + 1}. {task['title']} - {status}")

# Mark selected task as completed
def complete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["completed"] = True
        update_listbox()
        save_tasks()
    else:
        messagebox.showwarning("Select Task", "No task selected.")

# Delete selected task
def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_listbox()
        save_tasks()
    else:
        messagebox.showwarning("Select Task", "No task selected.")

# Initialize window
window = tk.Tk()
window.title("To-Do List App")
window.geometry("400x400")
window.resizable(False, False)

# Widgets
task_entry = tk.Entry(window, width=30)
task_entry.pack(pady=10)

add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack()

listbox = tk.Listbox(window, width=50)
listbox.pack(pady=10)

complete_button = tk.Button(window, text="Mark as Completed", command=complete_task)
complete_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Load tasks and start app
tasks = load_tasks()
update_listbox()
window.mainloop()