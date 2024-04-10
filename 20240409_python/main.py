import tkinter as tk
import datetime
from tkinter import ttk, messagebox

class Szemely:
    def __init__(self, azon, nev, szul_hely, szul_ido, nem):
        self.azon = azon
        self.nev = nev
        self.szul_hely = szul_hely
        self.szul_ido = szul_ido
        self.nem = nem

def szemelyek_olvas():
    szemelyek = []
    with open("szemelyek.txt", encoding="utf-8") as f:
        for line in f:
            szemelyek.append(Szemely(*line.strip().split("\t")))
    return szemelyek

def rokoni_fokozat_olvas():
    nemek = {"apa": "férfi", "anya": "nő", "nagybáty": "férfi", "nagynéni": "nő"}
    fokozatok = []
    with open("rokoni_fokozatok.txt", encoding="utf-8") as f:
        for line in f:
            fokozat, intervallum = line.strip().split("\t")
            hatarok = [int(n) for n in intervallum.split("-") if n]
            hatar = range(hatarok[0], hatarok[1]+1 if len(hatarok) == 2 else 10000)
            fokozatok.append((hatar, fokozat, nemek.get(fokozat, "")))
    return fokozatok

def fokozatok_szemelyekbol(fokozatok, szemely1, szemely2):
    # szemely1 az idősebb => szemely1.szul_ido < szemely2.szul_ido
    szul_ido1 = datetime.date.fromisoformat(szemely1.szul_ido.replace('.', '-'))
    szul_ido2 = datetime.date.fromisoformat(szemely2.szul_ido.replace('.', '-'))
    if szul_ido1 > szul_ido2:
        szemely1, szemely2 = szemely2, szemely1
        szul_ido1, szul_ido2 = szul_ido2, szul_ido1
    kapcsolat = []
    ido_kul = (szul_ido2 - szul_ido1).days // 365
    for hatar, fokozat, nem in fokozatok:
        if ido_kul in hatar and (not nem or (nem and szemely1.nem == nem)):
                kapcsolat.append(fokozat)
    return kapcsolat

def combobox_select(cur_list, other_list):
    prev = prev_idx[cur_list]
    cur_idx = cur_list.current()
    if cur_idx == other_list.current():
        messagebox.showerror("Hiba", "Két különböző személyt kell kiválasztani.")
        cur_idx = 1 if cur_idx == 0 else 0
        cur_list.current(prev if prev >= 0 else cur_idx)
    prev_idx[cur_list] = cur_idx

def button_clicked():
    nev1_idx = nev1_list.current()
    nev2_idx = nev2_list.current()
    if nev1_idx < 0 or nev2_idx < 0:
        messagebox.showerror("Hiba", "Legalább egy személyt ki kell választani.")
        return
    szemely1 = szemelyek[nev1_idx]
    szemely2 = szemelyek[nev2_idx]
    if szemely1.nev.split()[0] == szemely2.nev.split()[0] and szemely1.szul_hely == szemely2.szul_hely:
        szemely2str = lambda sz: f"{sz.nev};{sz.szul_hely};{sz.szul_ido}.;"
        messagebox.showinfo("Információ", "Valószínűleg rokonok.")
        kapcsolat = fokozatok_szemelyekbol(fokozatok, szemely1, szemely2)
        with open("rokonok.txt", "a", encoding="utf-8") as f:
            print('\n' + szemely2str(szemely1) + szemely2str(szemely2) + ';'.join(kapcsolat), end="", file=f)
    else:
        messagebox.showinfo("Információ", "Valószínűleg nem rokonok.")

szemelyek = szemelyek_olvas()
fokozatok = rokoni_fokozat_olvas()

root = tk.Tk()
root.title("Rokonság megállapítás")
root.geometry("440x400")

nevek = [sz.nev for sz in szemelyek]

nev1 = tk.StringVar()
nev2 = tk.StringVar()

nev1_list = ttk.Combobox(root, textvariable=nev1, values=nevek, state="readonly")
nev2_list = ttk.Combobox(root, textvariable=nev2, values=nevek, state="readonly")
gomb = tk.Button(root, text="Mehet!", command=button_clicked)

nev1_list.bind("<<ComboboxSelected>>", lambda e: combobox_select(nev1_list, nev2_list))
nev2_list.bind("<<ComboboxSelected>>", lambda e: combobox_select(nev2_list, nev1_list))

nev1_list.pack(side=tk.LEFT, anchor=tk.N)
nev2_list.pack(side=tk.RIGHT, anchor=tk.N)
gomb.pack()

prev_idx = {nev1_list: -1, nev2_list: -1}

root.mainloop()
