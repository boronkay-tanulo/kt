import random

class Nev:
    def __init__(self, lista, ertek=0): # ez egy konstruktor
        self.lista = lista
        self.ertek = ertek

    def eldontes(self):
        for elem in self.lista:
            if elem == self.ertek:
                return True
        return False

    def kivalasztas(self):
        if not self.eldontes():
            return -1
        for i in range(len(self.lista)):
            if self.lista[i] == self.ertek:
                return i

    def lin_keres(self):
        i = 0
        while i < len(self.lista) and self.lista[i] != self.ertek:
            i += 1
        return i

# HF: nem kell a rendezés
# FŐPROGRAM:
# példányosítjuk az osztályt
#n = Nev() # ez itt még nem tökéletes, mert LEGALÁBB egy listát kell adnunk!
def main():
    n = int(input("Kérem az elemszámot! "))
    a = int(input("Kérem az alsó határt! "))
    f = int(input("Kérem a felső határt! "))
    l = []
    for i in range(n):
        l.append(random.randint(a, f))
    i = int(input("Melyik elemre kíváncsi a listából? "))
    n = Nev(l, i)
    print(f"A(z) „{i}” elem {'megtalálható' if n.eldontes() else 'nem található meg'} a listában", end='' if n.eldontes() else '.')
    if (idx := n.kivalasztas()) > -1:
        print(f", indexe „{idx}”.")
    # TODO: befejezni

main()
