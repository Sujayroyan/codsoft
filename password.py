import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4.")
            return

        # Character pools
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation
        all_chars = lower + upper + digits + symbols

        # Ensure strong password by using all categories
        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(symbols)
        ] + random.choices(all_chars, k=length - 4)

        random.shuffle(password)
        result.set("".join(password))

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(result.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("350x250")
window.resizable(False, False)

# Title label
tk.Label(window, text="Strong Password Generator", font=("Arial", 14, "bold")).pack(pady=10)

# Password length input
tk.Label(window, text="Enter password length:", font=("Arial", 12)).pack()
length_entry = tk.Entry(window, font=("Arial", 12), justify="center")
length_entry.pack(pady=5)

# Generate button
tk.Button(window, text="Generate Password", font=("Arial", 12), command=generate_password).pack(pady=10)

# Result display
result = tk.StringVar()
tk.Entry(window, textvariable=result, font=("Arial", 12), justify="center", state="readonly", width=30).pack()

# Copy button
tk.Button(window, text="Copy to Clipboard", font=("Arial", 10), command=copy_to_clipboard).pack(pady=10)

# Run the application
window.mainloop()