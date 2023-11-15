class Adatok:
    def __init__(self, rend, r_latin, csalad, cs_latin, faj, f_latin, max_cm, min_Celsius=None, max_Celsius=None) -> None:
        self.rend = rend
        self.r_latin = r_latin
        self.csalad = csalad
        self.cs_latin = cs_latin
        self.faj = faj
        self.f_latin = f_latin
        self.max_cm = max_cm
        self.min_Celsius = min_Celsius
        self.max_Celsius = max_Celsius

halak = []

with open("akvariumi_halak.txt", encoding="ansi") as f:
    f.readline() # az első sort eldobjuk
    for line in f:
        adatok = line.strip().replace("(", "").replace(")", "").split("\t")
        halak.append(Adatok(*adatok))

for hal in halak:
    print(hal.faj)

megvan = False
while not megvan:
    hal_nev = input("Kérem válassza ki az egyik halfajt! ")
    for hal in halak:
        if hal.faj == hal_nev:
            megvan = True
            break
print(f"A hal latin neve: {hal.f_latin}. A hal rendje: {hal.rend}. A hal családja: {hal.csalad}. A hal maximum hossza: {hal.max_cm} cm.")

rendek = set()
for hal in halak:
    rendek.add(hal.rend)

for rend in rendek:
    print(rend)

megvan = False
while not megvan:
    rend_nev = input("Kérem válassza ki az egyik rendet! ")
    if rend_nev in rendek:
        megvan = True

csaladok = set()
fajok = []
for hal in halak:
    if hal.rend == rend_nev:
        csaladok.add(hal.csalad)
        fajok.append(hal)

print("A rendhez tartozó összes család:")
for csalad in csaladok:
    print(csalad)

print("A rendhez tartozó összes faj:")
for faj in fajok:
    print(f"A faj neve: {faj.faj}. A faj latin neve: {faj.f_latin}. " +
          f"A faj családjának neve: {faj.csalad}. A faj családjának latin neve: {faj.cs_latin}. A faj max hossza: {faj.max_cm} cm. " +
          (f"A faj ebben a hőmérséklet tartományban képes élni: {faj.min_Celsius}-{faj.max_Celsius} °C"
          if faj.min_Celsius is not None and faj.max_Celsius is not None else ""))
