import tkinter as tk
from tkinter import messagebox
import math
import random

colors = ["red", "yellow", "green", "blue", "violet", "orange"]

root = tk.Tk()
root.title("Színözön")
root.geometry("605x610")

canvas = tk.Canvas(root, width=600, height=610, bg="white")
canvas.pack()
circles = []
stored_colors = []
stored_idxs = []

_colors = colors.copy()
correct_colors = random.shuffle(_colors)
correct_colors = _colors[:4]

states = {"WON": 0, "LOST": 1, "PROGRESS": 2}
state = states["PROGRESS"]

for n in range(6):
    row = {'inputs': [], 'check': []}
    # bejövő színek
    row["inputs"].append(canvas.create_oval(10,  10 + n * 100, 100, 100 + n * 100))
    row["inputs"].append(canvas.create_oval(110, 10 + n * 100, 200, 100 + n * 100))
    row["inputs"].append(canvas.create_oval(210, 10 + n * 100, 300, 100 + n * 100))
    row["inputs"].append(canvas.create_oval(310, 10 + n * 100, 400, 100 + n * 100))
    # színek helyessége
    row["check"].append(canvas.create_oval(410, 10 + n * 100, 450,  50 + n * 100, outline="white"))
    row["check"].append(canvas.create_oval(410, 60 + n * 100, 450, 100 + n * 100, outline="white"))
    row["check"].append(canvas.create_oval(460, 10 + n * 100, 500,  50 + n * 100, outline="white"))
    row["check"].append(canvas.create_oval(460, 60 + n * 100, 500, 100 + n * 100, outline="white"))
    row["validate"] = canvas.create_rectangle(510, 10 + n * 100, 600, 100 + n * 100)
    row["text"] = canvas.create_text(555, 50 + n * 100, text="CHECK", fill="black", font=("Arial", 15))
    # elválasztó vonal
    circles.append(row)
    stored_colors.append(["white"] * 4)
    stored_idxs.append([-1] * 4)
    canvas.create_line(10, 5 + n * 100, 600, 5 + n * 100)

canvas.create_line(10, 5 + (n+1) * 100, 600, 5 + (n+1) * 100)
cur_idx = 0

def check_game_over(state):
    text = ""
    if state in {states["WON"], states["LOST"]}:
        text = "won" if state == states["WON"] else "lost"
    elif state == states["PROGRESS"] and cur_idx >= 6:
        state = states["LOST"]
        text = "lost"
    if text:
        messagebox.showinfo("Game Over!", f"You have {text} the game!")
        root.quit()

def click(event):
    global state
    global cur_idx
    for idx, input in enumerate(circles[cur_idx]['inputs']):
        coords = canvas.coords(input)
        center = (coords[0] + coords[2]) // 2, (coords[1] + coords[3]) // 2
        if math.dist((event.x, event.y), center) <= 45:
            stored_idxs[cur_idx][idx] = (stored_idxs[cur_idx][idx] + 1) % len(colors)
            stored_colors[cur_idx][idx] = colors[stored_idxs[cur_idx][idx]]
            canvas.itemconfig(input, fill=stored_colors[cur_idx][idx])
            return
    button_bbox = canvas.bbox(circles[cur_idx]['validate'])
    if all(map(lambda x: x != "white", stored_colors[cur_idx])) and \
              len(set(stored_colors[cur_idx])) == len(stored_colors[cur_idx]) and \
              button_bbox[0] <= event.x <= button_bbox[2] and \
              button_bbox[1] <= event.y <= button_bbox[3]:
        correct_num = 0
        exist_num = 0
        for stored, correct in zip(stored_colors[cur_idx], correct_colors):
            #print(stored, correct)
            if stored == correct:
                correct_num += 1
            elif stored in correct_colors:
                exist_num += 1
        #print(correct_num, exist_num)
        if correct_num == 4:
            state = states["WON"]
        for i in range(4):
            if correct_num > 0:
                correct_num -= 1
                canvas.itemconfig(circles[cur_idx]['check'][i], fill="black", outline="black")
            elif exist_num > 0:
                exist_num -= 1
                canvas.itemconfig(circles[cur_idx]['check'][i], fill="white", outline="black")
        cur_idx += 1
    check_game_over(state)

canvas.bind("<Button-1>", click)

root.mainloop()
