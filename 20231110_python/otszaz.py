with open('penztar.txt') as f:
    vasarlasok = f.read().strip().split('F')
    vasarlasok.pop()
    vasarlasok = [adat.strip().splitlines() for adat in vasarlasok]

print("2. feladat:")
print(f"A fizetések száma: {len(vasarlasok)}")

print("\n3. feladat:")
print(f"Az első vásárló {len(vasarlasok[0])} darab árucikket vásárolt.")

print("\n4. feladat:")
sorszam = int(input("Adja meg a vásárlás sorszámát! "))
arucikk = input("Adja meg egy árucikk nevét! ")
darabszam = int(input("Adja meg a vásárolt darabszámot! "))

print("\n5. feladat:")
def keres(l):
    for idx, vasarlas in enumerate(l):
        if arucikk in vasarlas:
            return idx
print(f"Az első vásárlás sorszáma: {keres(vasarlasok)+1}")
print(f"Az utolsó vásárlás sorszáma: {len(vasarlasok) - keres(reversed(vasarlasok))}")
mennyi = 0
for vasarlas in vasarlasok:
    if arucikk in vasarlas:
        mennyi += 1
print(f"{mennyi} vásárlás során vettek belőle.")

print("\n6. feladat:")
def ertek(darab):
    ossz = 0
    for i in range(darab):
        if i == 0:
            ossz += 500
        elif i == 1:
            ossz += 450
        else:
            ossz += 400
    return ossz
print(f"{darabszam} darab vételekor fizetendő: {ertek(darabszam)}")

print("\n7. feladat:")
arucikkek = {}
vasarlas = vasarlasok[sorszam-1]
for arucikk in vasarlas:
    arucikkek[arucikk] = arucikkek.get(arucikk, 0) + 1
for arucikk, darabszam in arucikkek.items():
    print(darabszam, arucikk)

with open('osszeg.txt', 'w') as f:
    for idx, vasarlas in enumerate(vasarlasok):
        arucikkek = {}
        for arucikk in vasarlas:
            arucikkek[arucikk] = arucikkek.get(arucikk, 0) + 1
        osszeg = 0
        for darabszam in arucikkek.values():
            osszeg += ertek(darabszam)
        print(f"{idx+1}: {osszeg}", file=f)
