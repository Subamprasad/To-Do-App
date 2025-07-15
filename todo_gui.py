import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import datetime
import json
import os

TASKS_FILE = "tasks.json"

PRIORITY_COLORS = {
    "High": "#ff6961",
    "Medium": "#fdfd96",
    "Low": "#77dd77"
}

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional To-Do App")
        self.root.geometry("500x500")
        self.root.configure(bg="#f0f4f8")
        self.tasks = []

        # Top bar with date and time
        self.top_frame = tk.Frame(root, bg="#4f8cff")
        self.top_frame.pack(fill=tk.X)
        self.datetime_label = tk.Label(self.top_frame, font=("Segoe UI", 14, "bold"), fg="white", bg="#4f8cff")
        self.datetime_label.pack(pady=8)
        self.update_datetime()

        # Entry and priority
        self.entry_frame = tk.Frame(root, bg="#f0f4f8")
        self.entry_frame.pack(pady=10)
        self.task_entry = ttk.Entry(self.entry_frame, width=30, font=("Segoe UI", 12))
        self.task_entry.pack(side=tk.LEFT, padx=(0, 10))
        self.priority_var = tk.StringVar(value="Medium")
        self.priority_menu = ttk.Combobox(self.entry_frame, textvariable=self.priority_var, values=["High", "Medium", "Low"], width=7, state="readonly")
        self.priority_menu.pack(side=tk.LEFT, padx=(0, 10))
        self.add_button = tk.Button(self.entry_frame, text="Add Task", command=self.add_task, bg="#4f8cff", fg="white", font=("Segoe UI", 10, "bold"), activebackground="#357ae8")
        self.add_button.pack(side=tk.LEFT)

        # Listbox with scrollbar
        self.list_frame = tk.Frame(root, bg="#f0f4f8")
        self.list_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox = tk.Listbox(self.list_frame, width=50, height=12, font=("Segoe UI", 12), activestyle='none', yscrollcommand=self.scrollbar.set, selectbackground="#b3d1ff")
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.bind('<Double-1>', self.edit_task)

        # Buttons
        self.button_frame = tk.Frame(root, bg="#f0f4f8")
        self.button_frame.pack(pady=10)
        self.done_button = tk.Button(self.button_frame, text="Mark as Done", command=self.mark_done, bg="#77dd77", fg="black", font=("Segoe UI", 10, "bold"), activebackground="#44c767")
        self.done_button.pack(side=tk.LEFT, padx=5)
        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task, bg="#ff6961", fg="white", font=("Segoe UI", 10, "bold"), activebackground="#e74c3c")
        self.delete_button.pack(side=tk.LEFT, padx=5)
        self.clear_button = tk.Button(self.button_frame, text="Clear All", command=self.clear_all, bg="#fdfd96", fg="black", font=("Segoe UI", 10, "bold"), activebackground="#fff700")
        self.clear_button.pack(side=tk.LEFT, padx=5)

        self.load_tasks()
        self.update_listbox()

    def update_datetime(self):
        now = datetime.datetime.now().strftime("%A, %d %B %Y | %H:%M:%S")
        self.datetime_label.config(text=now)
        self.root.after(1000, self.update_datetime)

    def add_task(self):
        task = self.task_entry.get().strip()
        priority = self.priority_var.get()
        if task:
            self.tasks.append({"task": task, "done": False, "priority": priority})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def mark_done(self):
        selected = self.listbox.curselection()
        if selected:
            idx = selected[0]
            self.tasks[idx]["done"] = not self.tasks[idx]["done"]
            self.update_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("Selection Error", "Please select a task.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            idx = selected[0]
            del self.tasks[idx]
            self.update_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("Selection Error", "Please select a task.")

    def clear_all(self):
        if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
            self.tasks.clear()
            self.update_listbox()
            self.save_tasks()

    def edit_task(self, event):
        selected = self.listbox.curselection()
        if selected:
            idx = selected[0]
            old_task = self.tasks[idx]["task"]
            old_priority = self.tasks[idx]["priority"]
            new_task = simpledialog.askstring("Edit Task", "Edit your task:", initialvalue=old_task)
            if new_task is not None and new_task.strip():
                new_priority = simpledialog.askstring("Edit Priority (High/Medium/Low)", "Edit priority:", initialvalue=old_priority)
                if new_priority and new_priority in PRIORITY_COLORS:
                    self.tasks[idx]["task"] = new_task.strip()
                    self.tasks[idx]["priority"] = new_priority
                    self.update_listbox()
                    self.save_tasks()
                else:
                    messagebox.showwarning("Priority Error", "Priority must be High, Medium, or Low.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task["done"] else "✗"
            color = PRIORITY_COLORS.get(task["priority"], "#ffffff")
            display = f"[{status}] {task['task']} ({task['priority']})"
            self.listbox.insert(tk.END, display)
            self.listbox.itemconfig(tk.END, {'bg': color, 'fg': 'black'})

    def save_tasks(self):
        try:
            with open(TASKS_FILE, "w", encoding="utf-8") as f:
                json.dump(self.tasks, f)
        except Exception as e:
            messagebox.showerror("Save Error", f"Could not save tasks: {e}")

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            try:
                with open(TASKS_FILE, "r", encoding="utf-8") as f:
                    self.tasks = json.load(f)
            except Exception:
                self.tasks = []

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use('clam')
    app = TodoApp(root)
    root.mainloop() 