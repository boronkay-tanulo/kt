import tkinter as tk

def open_map(fname):
    map_l = []
    with open(fname, "r", encoding="utf-8") as f:
        for line in f:
            space_count = line.count(" ")
            if space_count == 0: # Az utolsó sor
                path = line
            elif space_count == 1: # Kezdő pozíció
                row, column = line.strip().split(" ")
            else: # Az összes többi sor
                map_l.append(line.strip().split(" "))
    return map_l, int(row), int(column), path

# Egy label méretének megállapítása
def get_label_size():
    dummy = tk.Label(text="69", font=("Times New Roman", 14), bg="red")
    label_width = dummy.winfo_reqwidth()
    label_height = dummy.winfo_reqheight() - 7
    dummy.destroy()
    return label_width, label_height

# Az ablak méretének meghatározása
def set_window_size(master, label_width, label_height, table_width, table_height, btn_height):
    full_width = label_width * table_width
    full_height = label_height * table_height + 5
    master.geometry(f"{full_width}x{full_height+btn_height}")

# label-ek hozzáadása
def place_labels(table, label_width, label_height):
    label_map = []
    for y, row in enumerate(table):
        new_row = []
        for x, num in enumerate(row):
            label = tk.Label(text=str(num), font=("Times New Roman", 14))
            label.place(x=x*label_width, y=y*label_height)
            new_row.append(label)
        label_map.append(new_row)
    return label_map

# Kirajzoló gomb lehelyezése
def place_button(master):
    btn = tk.Button(master, text="Útvonal megjelenítése", command=lambda: color_labels(column, line, labels, path))
    btn.pack(side=tk.BOTTOM, fill=tk.X)
    return btn

# label-ek kiszínezése
def color_labels(x, y, label_map, path):
    labels[y][x].config(bg="green")
    for c in path:
        prev_val = int(table[y][x])
        if c == "L":
            y += 1
        elif c == "J":
            x += 1
        cur_val = int(table[y][x])
        if cur_val < prev_val: # csökken a magasság
            color = "lightgreen"
        elif cur_val > prev_val: # nő a magasság
            color = "darkgreen"
        else: # nem változik a magasság
            color = "green"    
        labels[y][x].config(bg=color)

table, line, column, path = open_map(input("Kérem a térkép fájl nevét! "))
#print(table)

# Ablak létrehozás
root = tk.Tk()
root.title("Útvonal kirajzoló")
root.attributes("-topmost", True)
root.resizable(False, False)

label_w, label_h = get_label_size()
labels = place_labels(table, label_w, label_h)
btn = place_button(root)
set_window_size(root, label_w, label_h, len(table[0]), len(table), btn.winfo_reqheight())
root.mainloop()