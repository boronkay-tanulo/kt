class Helyezes:
    def __init__(self, helyezes, sportolok_szama, sportag, versenyszam):
        self.helyezes = helyezes
        self.sportolok_szama = sportolok_szama
        self.sportag = sportag
        self.versenyszam = versenyszam

# 2. feladat
adatok = []
with open("helsinki.txt", 'r') as f:
    for sor in f:
        info = sor.strip().split()
        adatok.append(Helyezes(int(info[0]), int(info[1]), info[2], info[3]))

# 3. feladat
print("3. feladat:")
print(f"Pontszerző helyezések száma: {len(adatok)}")

# 4. feladat
print("4. feladat:")
arany = 0
ezust = 0
bronz = 0
for adat in adatok:
    if adat.helyezes == 1:
        arany += 1
    elif adat.helyezes == 2:
        ezust += 1
    elif adat.helyezes == 3:
        bronz += 1
print(f"Arany: {arany}")
print(f"Ezüst: {ezust}")
print(f"Bronz: {bronz}")
print(f"Összesen: {arany + ezust + bronz}")

# 5. feladat
print("5. feladat:")
pontszamok = {1: 7, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
pontszam = 0
for adat in adatok:
    pontszam += pontszamok[adat.helyezes]
print(f"Olimpiai pontok száma: {pontszam}")

# 6. feladat
print("6. feladat:")
torna = 0
uszas = 0
for adat in adatok:
    if adat.helyezes <= 3:
        if adat.sportag == "torna":
            torna += 1
        elif adat.sportag == "uszas":
            uszas += 1

if torna > uszas:
    print("Torna sportágban szereztek több érmét.")
elif torna < uszas:
    print("Úszás sportágban szereztek több érmét.")
else:
    print("Egyenlő volt az érmék száma.")

# 7. feladat
with open("helsinki2.txt", 'w') as f:
    for adat in adatok:
        pont = pontszamok[adat.helyezes]
        print(f"{adat.helyezes} {adat.sportolok_szama} {pont} {'kajak-kenu' if adat.sportag == 'kajakkenu' else adat.sportag} {adat.versenyszam}", file=f)

# 8. feladat
print("8. feladat:")
legtobb = max(adatok, key=lambda x: x.sportolok_szama)
print(f"Helyezés: {legtobb.helyezes}")
print(f"Sportág: {legtobb.sportag}")
print(f"Versenyszám: {legtobb.versenyszam}")
print(f"Sportolók száma: {legtobb.sportolok_szama}")
