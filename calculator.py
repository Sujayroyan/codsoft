import tkinter as tk

# Button click handler
def on_click(symbol):
    current = entry.get()
    if symbol == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif symbol == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, symbol)

# Create main window
window = tk.Tk()
window.title("Traditional Calculator")
window.geometry("300x400")
window.resizable(False, False)

# Entry display
entry = tk.Entry(window, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

# Button layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+"),
    ("C",)
]

# Create buttons dynamically
for r, row in enumerate(buttons, start=1):
    for c, btn_text in enumerate(row):
        btn = tk.Button(window, text=btn_text, width=5, height=2,
                        font=("Arial", 16),
                        command=lambda symbol=btn_text: on_click(symbol))
        btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

# Adjust column weights for even spacing
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# Run the application
window.mainloop()