class Termek:
    def __init__(self, nev, nettoAr, afaKulcs):
        self.nev = nev
        self.nettoAr = nettoAr
        self.afaKulcs = afaKulcs
    def bruttoArKiszamol(self):
        return self.nettoAr * (1 + (0.01 * self.afaKulcs))

termekek = []
print("3. feladat")
for i in range(3):
    nev = input(f"Adja meg a(z) {i+1}. termék nevét:\n")
    netto_ar = input(f"Adja meg a(z) {i+1}. termék nettó árát:\n")
    afa_kulcs = input(f"Adja meg a(z) {i+1}. termék áfakulcsát:\n")
    termek = Termek(nev, int(netto_ar), int(afa_kulcs))
    termekek.append(termek)

for termek in termekek:
    print(f"Termék neve: {termek.nev}, nettó ár: {termek.nettoAr} Ft, áfakulcs: {termek.afaKulcs}%, bruttó ár: {termek.bruttoArKiszamol()} Ft")
    
