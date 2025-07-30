import tkinter as tk
from tkinter import messagebox

# Create main window
window = tk.Tk()
window.title("Tic Tac Toe - Colorful")
window.resizable(False, False)

# Set starting player
current_player = "X"

# Board setup
buttons = [[None for _ in range(3)] for _ in range(3)]

# Function to check for a winner
def check_winner():
    for i in range(3):
        # Rows
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        # Columns
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    # Diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

# Check for a draw
def check_draw():
    return all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3))

# On button click
def on_click(row, col):
    global current_player

    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player

        # Set color
        if current_player == "X":
            buttons[row][col]["fg"] = "red"
        else:
            buttons[row][col]["fg"] = "green"

        buttons[row][col]["state"] = "disabled"

        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Reset game
def reset_game():
    global current_player
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j]["state"] = "normal"
            buttons[i][j]["fg"] = "black"

# Create buttons grid
for i in range(3):
    for j in range(3):
        button = tk.Button(window, text="", font=('Arial', 24), width=5, height=2,
                           command=lambda row=i, col=j: on_click(row, col))
        button.grid(row=i, column=j)
        buttons[i][j] = button

# Start GUI loop
window.mainloop()
