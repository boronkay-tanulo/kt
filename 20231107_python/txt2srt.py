class IdozitettFelirat:
    def __init__(self, idozites, felirat):
        self.idozites = idozites
        self.felirat = felirat
        self.SzavakSzama = len(self.felirat.split())
    def SrtIdozites(self):
        kezd, veg = map(lambda n: self.__atalakit(n.strip()), self.idozites.split('-'))
        return f"{kezd} --> {veg}"
    @staticmethod
    def __atalakit(ido):
        perc, mperc = map(lambda n: int(n), ido.split(':'))
        ora, perc = divmod(perc, 60)
        return f"{ora:0>2}:{perc:0>2}:{mperc:0>2}"

adatok = []
with open("feliratok.txt", "r") as f:
    for i, sor in enumerate(f):
        if i % 2 == 0:
            idozites = sor.strip()
        else:
            felirat = sor.strip()
            adatok.append(IdozitettFelirat(idozites, felirat))

print("5. feladat:")
print(f"A fájlban {len(adatok)} felirat van.")

print("7. feladat:")
legtobb_szo = max(adatok, key=lambda n: n.SzavakSzama)
print(f"A legtöbb szóból álló mondat {legtobb_szo.SzavakSzama} szóból áll.")

with open("felirat.srt", "w") as f:
    for i, felirat in enumerate(adatok):
        print(f"{i+1}\n{felirat.SrtIdozites()}\n{felirat.felirat}\n", file=f)
