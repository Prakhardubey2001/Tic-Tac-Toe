import tkinter as tk
from tkinter import messagebox

def check_win():
    global winner
    for combination in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combination[0]]["text"] == buttons[combination[1]]["text"] == buttons[combination[2]]["text"] != "":
            for i in combination:
                buttons[i].config(bg='green')
            messagebox.showinfo("Congratulations", f"Player {buttons[combination[0]]['text']} wins! 😊")
            winner = True
            root.quit()
            return

    # Check for a tie
    if all(button["text"] != "" for button in buttons) and not winner:
        messagebox.showinfo("Tie", "The game is a tie!")
        root.quit()

def button_click(index):
    if buttons[index]['text'] == "" and not winner:
        buttons[index]['text'] = current_player
        check_win()
        toggle_players()

def toggle_players():
    global current_player
    current_player = "❌" if current_player == "✔️" else "✔️"
    label.config(text=f'Player {current_player} turn')

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)

current_player = "❌"
winner = False
label = tk.Label(root, text=f'Player {current_player} turn', font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
