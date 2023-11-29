import tkinter as tk
from tkinter import ttk

def mehet_click():
    also_ = also.get()
    felso_ = felso.get()
    oszto_ = oszto.get()
    # lb_1 feltöltése
    lb_1.delete(0, tk.END) # kipucolom lb_1-et, hátha van már benne valami
    for szam in range(also_, felso_+1):
        lb_1.insert(tk.END, szam)
        if szam % oszto_ == 0:
            lb_1.itemconfig(tk.END, {"bg": "red", "fg": "white"})
    # lb_2 feltöltése
    lb_2.delete(0, tk.END)
    for szam in range(also_, felso_+1):
        if szam % oszto_ == 0:
            lb_2.insert(tk.END, szam)
    

# Főablak
ablak = tk.Tk()
ablak.title("Listbox & NumericUpDown")
ablak.geometry("350x400")

betutipus = ("Calibri", 15, "")

# NumericUpDown vezérlők
also = tk.IntVar()
felso = tk.IntVar()
oszto = tk.IntVar()

nud_1 = ttk.Spinbox(ablak, from_=0, to=50, textvariable=also, font=betutipus)
nud_2 = ttk.Spinbox(ablak, from_=0, to=50, textvariable=felso, font=betutipus)
nud_3 = ttk.Spinbox(ablak, from_=1, to=50, textvariable=oszto, font=betutipus)

nud_1.place(x=10, y=10, width=80, height=30)
nud_2.place(x=100, y=10, width=80, height=30)
nud_3.place(x=190, y=10, width=80, height=30)

# Gomb létrehozása
gomb_1 = tk.Button(ablak, text="Mehet!", command=mehet_click, font=betutipus)
gomb_1.place(x=190, y=40, width=80, height=30)

lb_1 = tk.Listbox(ablak, font=betutipus)
lb_2 = tk.Listbox(ablak, font=betutipus)

lb_1.place(x=10, y=50, width=80, height=300)
lb_2.place(x=100, y=50, width=80, height=300)

ablak.mainloop()
