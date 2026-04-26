import tkinter as tk
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.agent import run_agent


def on_submit():
    user_input = text_box.get("1.0", tk.END)

    if not user_input.strip():
        messagebox.showwarning("Warning", "Please enter a request")
        return

    issue_key = run_agent(user_input)

    if "Error" in issue_key:
        messagebox.showerror("Error", issue_key)
    else:
        messagebox.showinfo("Success", f"Ticket Created: {issue_key}")


root = tk.Tk()
root.title("Jira Agent")
root.geometry("600x400")

label = tk.Label(root, text="Enter your request:", font=("Arial", 14))
label.pack(pady=10)

# 🔥 INPUT FIELD (THIS WILL DEFINITELY SHOW)
text_box = tk.Text(root, height=8, width=70)
text_box.pack(pady=10)

button = tk.Button(root, text="Create Ticket", command=on_submit)
button.pack(pady=20)

root.mainloop()