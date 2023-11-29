import tkinter as tk
from tkinter import ttk # themes tkinter - szofisztikáltabb vezérlők

def szin_valasztas(event):
    if cb_ertek.get() == "piros":
        szin = "red"
    elif cb_ertek.get() == "zöld":
        szin = "green"
    else:
        szin = "blue"
    ablak.config(background=szin)

# FŐPROGRAM
# ablak (főablak) létrehozása
ablak = tk.Tk()
ablak.title("Színválasztó")
ablak.geometry("600x400+-600+-400")

# ComboBox létrehozása
alapszinek = ["piros", "zöld", "kék"]
cb_ertek = tk.StringVar()
combo_box = ttk.Combobox(ablak, textvariable=cb_ertek, values=alapszinek, state="readonly")
combo_box.place(x=10, y=10, width=100, height=30)
# A "bind" egy függvény, amely összeköt egy eseményt egy eseménykezelővel.
combo_box.bind("<<ComboboxSelected>>", szin_valasztas)

# ablak ciklusának indítása. "Főciklus", ami végtelen.
ablak.mainloop() # az utolsó utasítás
