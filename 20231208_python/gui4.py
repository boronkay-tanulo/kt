import tkinter as tk
from tkinter import messagebox

class SzamlaloAlkalmazas:
    def __init__(self, ablak):
        self.ablak = ablak
        self.ablak.title("Számláló Alkalmazás")
        self.ablak.geometry("400x200")
        self.r = 0
        self.g = 0
        self.b = 0
        self.ablak.configure(bg="black")
        self.ertek = tk.IntVar() # a kiírt szám változója
        self.ertek.set(0) # a kezdőérték beállítása
        gomb_novel = tk.Button(ablak, text="Növel", font=("Times", 20), command=self.novel)
        gomb_csokkent = tk.Button(ablak, text="Csökkent", font=("Times", 20), command=self.csokkent)
        gomb_novel.pack(side=tk.LEFT, padx=10)
        gomb_csokkent.pack(side=tk.RIGHT, padx=10)
        self.cimke = tk.Label(ablak, font=("Times", 24), textvariable=self.ertek)
        self.cimke.pack(side=tk.BOTTOM, pady=80)
    def novel(self):
        self.ertek.set(self.ertek.get() + 1)
        self.set_rgb(1)
        self.ablak.configure(bg=self.rgb2hex())
        #print(self.r, self.g, self.b)
    def csokkent(self):
        e = self.ertek.get()
        if e > 0:
            self.ertek.set(e - 1)
        self.set_rgb(-1)
        self.ablak.configure(bg=self.rgb2hex())
        #print(self.r, self.g, self.b)
    def set_rgb(self, add):
        e = self.ertek.get()
        if add > 0:
            if 0 <= self.r + add <= 255:
                self.r += add
            elif 0 <= self.g + add <= 255 and self.r == 255:
                self.g += add
            elif 0 <= self.b + add <= 255 and self.g == self.r == 255:
                self.b += add
        elif add < 0:
            if 0 <= self.b + add <= 255:
                self.b += add
            elif 0 <= self.g + add <= 255 and self.b == 0:
                self.g += add
            elif 0 <= self.r + add <= 255 and self.g == self.b == 0:
                self.r += add
        if self.r == self.g == self.b == 255:
            self.ertek.set(765)
            messagebox.showinfo("Üzenet", "Innentől fehér vagyok.")
    def rgb2hex(self):
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

# FŐPROGRAM
if __name__ == "__main__":
    ablak = tk.Tk()
    alkalmazas = SzamlaloAlkalmazas(ablak)
    ablak.mainloop()
