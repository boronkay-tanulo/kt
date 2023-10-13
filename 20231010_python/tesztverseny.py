# 1. feladat
data = {}
with open("valaszok.txt", "r") as f:
    for i, line in enumerate(f):
        if i == 0:
            jo_valasz = line.strip()
            continue
        k, v = line.strip().split()
        data[k] = v

# 2. feladat
print("2. feladat: ", end="")
print(f"A vetélkedőn {len(data)} versenyző indult.\n")

# 3. feladat
print("3. feladat: ", end="")
azonosito = input("A versenyző azonosítója = ")
valasz = data[azonosito]
print(f"{valasz}   (a versenyző válasza)\n")

# 4. feladat
print("4. feladat: ")
print(f"{jo_valasz}   (a helyes megoldás)")
for c1, c2 in zip(valasz, jo_valasz):
    print(end="+" if c1 == c2 else " ")
print("   (a versenyző helyes válaszai)\n")

# 5. feladat
print("5. feladat: ", end="")
idx = int(input("A feladat sorszáma = ")) - 1
helyes = 0
for v in data.values():
    if v[idx] == jo_valasz[idx]:
        helyes += 1
print(f"A feladatra {helyes} fő, a versenyzők {helyes / len(data) * 100:.2f}%-a adott helyes választ.\n")

# 6. feladat
pontszamok = {}
with open("pontok.txt", "w") as f:
    for k, v in data.items():
        pontszam = 0
        for i, cs in enumerate(zip(v, jo_valasz)):
            c1, c2 = cs
            if c1 == c2:
                if 0 <= i <= 4:
                    pontszam += 3
                elif 5 <= i <= 9:
                    pontszam += 4
                elif 10 <= i <= 12:
                    pontszam += 5
                elif i == 13:
                    pontszam += 6
        pontszamok[k] = pontszam
        print(f"{k} {pontszam}", file=f)

# 7. feladat
print("7. feladat: A verseny legjobbjai:")
rendez_pontszamok = dict(sorted(pontszamok.items(), key=lambda pair: pair[1], reverse=True))
nyertesek = {}
elozo = -1
helyezetek = 0
for k, v in rendez_pontszamok.items():
    if helyezetek >= 3: break
    if elozo != v:
        elozo = v
        helyezetek += 1
    nyertesek[k] = (v, helyezetek)

for k, v in nyertesek.items():
    pont, dij = v
    print(f"{dij}. ({pont} pont): {k}")

