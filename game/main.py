from tkinter import *
from tkinter import ttk
import random  as rnd

player = rnd.randint(1, 2)
player1 = "Ход первого игрока"
player2 = "Ход второго игрока"
result = {
    1: {1: "?", 2: "?", 3: "?"},
    2: {1: "?", 2: "?", 3: "?"},
    3: {1: "?", 2: "?", 3: "?"}
}

victoryComb = {
    1: {1: {"x": 1, "y": 1}, 2: {"x": 1, "y": 2}, 3: {"x": 1, "y": 3}},
    2: {1: {"x": 2, "y": 1}, 2: {"x": 2, "y": 2}, 3: {"x": 2, "y": 3}},
    3: {1: {"x": 3, "y": 1}, 2: {"x": 3, "y": 2}, 3: {"x": 3, "y": 3}},
    4: {1: {"x": 1, "y": 1}, 2: {"x": 2, "y": 1}, 3: {"x": 3, "y": 1}},
    5: {1: {"x": 1, "y": 2}, 2: {"x": 2, "y": 2}, 3: {"x": 3, "y": 2}},
    6: {1: {"x": 1, "y": 3}, 2: {"x": 2, "y": 3}, 3: {"x": 3, "y": 3}},
    7: {1: {"x": 1, "y": 1}, 2: {"x": 2, "y": 2}, 3: {"x": 3, "y": 3}},
    8: {1: {"x": 3, "y": 1}, 2: {"x": 2, "y": 2}, 3: {"x": 1, "y": 3}},
}

def verificationResult():
    global victoryComb
    global result
    global player
    for i in victoryComb:
        fp = "0" if player == 1 else "X"
        if result[victoryComb[i][1]["x"]][victoryComb[i][1]["y"]] == fp and result[victoryComb[i][2]["x"]][victoryComb[i][2]["y"]] == fp and result[victoryComb[i][3]["x"]][victoryComb[i][3]["y"]] == fp:
            return True
    return False

def verificationClick(name):
    global result
    if name == "lbl1":
        return True if result[1][1] == "?" else False
    elif name == "lbl2":
        return True if result[1][2] == "?" else False
    elif name == "lbl3":
        return True if result[1][3] == "?" else False
    elif name == "lbl4":
        return True if result[2][1] == "?" else False
    elif name == "lbl5":
        return True if result[2][2] == "?" else False
    elif name == "lbl6":
        return True if result[2][3] == "?" else False
    elif name == "lbl7":
        return True if result[3][1] == "?" else False
    elif name == "lbl8":
        return True if result[3][2] == "?" else False
    elif name == "lbl9":
        return True if result[3][3] == "?" else False

def ff(event, name):
    global player
    if not verificationClick(name):
        return
    if name == "lbl1":
        result[1][1] = "0" if player == 1 else "X"
        lbl1["text"] = "0" if player == 1 else "X"
        lbl1["fg"] = "red" if player == 1 else "green"
    elif name == "lbl2":
        result[1][2] = "0" if player == 1 else "X"
        lbl2["text"] = "0" if player == 1 else "X"
        lbl2["fg"] = "red" if player == 1 else "green"
    elif name == "lbl3":
        result[1][3] = "0" if player == 1 else "X"
        lbl3["text"] = "0" if player == 1 else "X"
        lbl3["fg"] = "red" if player == 1 else "green"
    elif name == "lbl4":
        result[2][1] = "0" if player == 1 else "X"
        lbl4["text"] = "0" if player == 1 else "X"
        lbl4["fg"] = "red" if player == 1 else "green"
    elif name == "lbl5":
        result[2][2] = "0" if player == 1 else "X"
        lbl5["text"] = "0" if player == 1 else "X"
        lbl5["fg"] = "red" if player == 1 else "green"
    elif name == "lbl6":
        result[2][3] = "0" if player == 1 else "X"
        lbl6["text"] = "0" if player == 1 else "X"
        lbl6["fg"] = "red" if player == 1 else "green"
    elif name == "lbl7":
        result[3][1] = "0" if player == 1 else "X"
        lbl7["text"] = "0" if player == 1 else "X"
        lbl7["fg"] = "red" if player == 1 else "green"
    elif name == "lbl8":
        result[3][2] = "0" if player == 1 else "X"
        lbl8["text"] = "0" if player == 1 else "X"
        lbl8["fg"] = "red" if player == 1 else "green"
    elif name == "lbl9":
        result[3][3] = "0" if player == 1 else "X"
        lbl9["text"] = "0" if player == 1 else "X"
        lbl9["fg"] = "red" if player == 1 else "green"
    if not verificationResult():
        if player == 1:
            player = 2
            lb["text"] = player2
        else:
            player = 1
            lb["text"] = player1
    else:
        lb["text"] = "Игрок 1 выиграл" if player == 1 else "Игрок 2 выиграл"

window = Tk()
window.title("Игра крестики-нолики")
window.geometry("400x400")

cellWidth = 10
cellHeight = 5
px=10
py=10
color = "white"


lb = Label(window, text=player1 if player == 1 else player2, fg='red', font=("Arial", 16, 'bold'))
lb.grid(column=0, row=0)

frame = ttk.LabelFrame(window)
frame.grid(column=0, row=1, padx=20, pady=20)

lbl1 = Label(frame, borderwidth=2, relief = "raised", width=cellWidth, height=cellHeight, text = "?", fg='blue', bg=color)
lbl1.grid(column=0, row=0, padx=px, pady=py)
lbl1.bind('<Button-1>', lambda event: ff(event, "lbl1"))

lbl2 = Label(frame, borderwidth=2, relief = "raised", width=cellWidth, height=cellHeight, text = "?", fg='blue', bg=color)
lbl2.grid(column=1, row=0, padx=px, pady=py)
lbl2.bind('<Button-1>', lambda event: ff(event, "lbl2"))

lbl3 = Label(frame, borderwidth=2, relief = "raised", width=cellWidth, height=cellHeight, text = "?", fg='blue', bg=color)
lbl3.grid(column=2, row=0, padx=px, pady=py)
lbl3.bind('<Button-1>', lambda event: ff(event, "lbl3"))

lbl4 = Label(frame, borderwidth=2, relief = "raised", width=cellWidth, height=cellHeight, text = "?", fg='blue', bg=color)
lbl4.grid(column=0, row=1, padx=px, pady=py)
lbl4.bind('<Button-1>', lambda event: ff(event, "lbl4"))

lbl5 = Label(frame, borderwidth=2, relief = "raised", width=cellWidth, height=cellHeight, text = "?", fg='blue', bg=color)
lbl5.grid(column=1, row=1, padx=px, pady=py)
lbl5.bind('<Button-1>', lambda event: ff(event, "lbl5"))

lbl6 = Label(frame, borderwidth=2, relief = "raised", width=cellWidth, height=cellHeight, text = "?", fg='blue', bg=color)
lbl6.grid(column=2, row=1, padx=px, pady=py)
lbl6.bind('<Button-1>', lambda event: ff(event, "lbl6"))

lbl7 = Label(frame, borderwidth=2, relief = "raised", width=cellWidth, height=cellHeight, text = "?", fg='blue', bg=color)
lbl7.grid(column=0, row=2, padx=px, pady=py)
lbl7.bind('<Button-1>', lambda event: ff(event, "lbl7"))

lbl8 = Label(frame, borderwidth=2, relief = "raised", width=cellWidth, height=cellHeight, text = "?", fg='blue', bg=color)
lbl8.grid(column=1, row=2, padx=px, pady=py)
lbl8.bind('<Button-1>', lambda event: ff(event, "lbl8"))

lbl9 = Label(frame, borderwidth=2, relief = "raised", width=cellWidth, height=cellHeight, text = "?", fg='blue', bg=color)
lbl9.grid(column=2, row=2, padx=px, pady=py)
lbl9.bind('<Button-1>', lambda event: ff(event, "lbl9"))

window.mainloop()