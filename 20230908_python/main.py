from datetime import date

class Adat:
    def __init__(self, nev, szul_datum, szul_hely, anya):
        self.nev = nev
        self.szul_datum = szul_datum
        self.szul_hely = szul_hely
        self.anya = anya

def beolvas(f):
    ret = []
    with open(f, "r", encoding="utf-8") as file:
        for line in file:
            ret.append(Adat(*line.strip().split(";")))
    ret.pop(0)
    return ret

l = beolvas("nyersanyag.txt")
for adat in l:
    szul_date = date(*[int(i) for i in adat.szul_datum.split('-')])
    kor = date.today().year - szul_date.year
    if date.today().month <= szul_date.month and date.today().day < szul_date.day:
        kor -= 1
    print(f"Név = {adat.nev}, jelenlegi életkora = {kor}, születési dátum = {adat.szul_datum}")

#a = Adat()
