import tkinter as tk
import random

# Choices with emojis
choices = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

# Score counters
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(list(choices.keys()))

    result_text = ""

    if user_choice == computer_choice:
        result_text = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Scissors" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        result_text = "You Win!"
        user_score += 1
    else:
        result_text = "Computer Wins!"
        computer_score += 1

    # Display choices and result with symbols
    result_var.set(
        f"You: {user_choice} {choices[user_choice]}\n"
        f"Computer: {computer_choice} {choices[computer_choice]}\n\n"
        f"{result_text}"
    )
    score_var.set(f"Score - You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_var.set("Make your move!")
    score_var.set("Score - You: 0 | Computer: 0")

# Window setup
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("400x420")
window.resizable(False, False)

tk.Label(window, text="Rock 🪨  Paper 📄  Scissors ✂️", font=("Arial", 16, "bold")).pack(pady=10)

# Result and score labels
result_var = tk.StringVar()
result_var.set("Make your move!")
tk.Label(window, textvariable=result_var, font=("Arial", 12), justify="center").pack(pady=10)

score_var = tk.StringVar()
score_var.set("Score - You: 0 | Computer: 0")
tk.Label(window, textvariable=score_var, font=("Arial", 12)).pack(pady=5)

# Game buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

tk.Button(button_frame, text="🪨 Rock", width=12, font=("Arial", 12), command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="📄 Paper", width=12, font=("Arial", 12), command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="✂️ Scissors", width=12, font=("Arial", 12), command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

# Reset button
tk.Button(window, text="🔁 Reset Game", font=("Arial", 11), command=reset_game).pack(pady=20)

# Start app
window.mainloop()