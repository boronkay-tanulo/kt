import tkinter as tk
from tkinter import messagebox
import random

def kattint():
    messagebox.showinfo("Gratulálok!", "Ügyes vagy!")
    ablak.destroy()

def mutat(event):
    uj_x = random.randint(5, ablak.winfo_width() - 5 - gomb.winfo_width())
    uj_y = random.randint(5, ablak.winfo_height() - 5 - gomb.winfo_height())
    gomb.place(x=uj_x, y=uj_y)

# Főablak
ablak = tk.Tk()
ablak.title("Bolond gomb")
ablak.geometry("600x400")

gomb = tk.Button(ablak, text="kattints!", width=8, height=2, command=kattint)
gomb.place(x=10, y=10)
gomb.bind("<Enter>", mutat)

ablak.mainloop()
