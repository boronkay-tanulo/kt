class Szelveny:
    def __init__(self, sz1, sz2, sz3, sz4, sz5):
        self.sz1 = sz1
        self.sz2 = sz2
        self.sz3 = sz3
        self.sz4 = sz4
        self.sz5 = sz5

def beolvas(fname):
    with open(fname, "r") as f:
        data = f.read().splitlines()
    data = [Szelveny(*[int(k) for k in sz.split(" ")]) for sz in data]
    return data

# 1. és 2. FELADAT
het52 = sorted([89, 24, 34, 11, 64])
jo_szamok = False
while not jo_szamok:
    szamok = [int(n) for n in input("Kérem az 52. hét számait, szőközzel elválasztva! ").split(" ")]
    szamok.sort()
    jo_szamok = szamok == het52

print("A lottószámok rendezve:", *szamok)
# 3. és 4. FELADAT
lottoszamok = beolvas("lottosz.dat")
het = int(input("Melyik hétnek kéri a lottószámait? (1-51) "))
heti_szamok = lottoszamok[het-1]
print(f"A {het}. hét lottószámai: {heti_szamok.sz1} {heti_szamok.sz2} {heti_szamok.sz3} {heti_szamok.sz4} {heti_szamok.sz5}")
# 5. FELADAT
kihuzott_szamok = {}
for szelveny in lottoszamok:
    kihuzott_szamok[szelveny.sz1] = True
    kihuzott_szamok[szelveny.sz2] = True
    kihuzott_szamok[szelveny.sz3] = True
    kihuzott_szamok[szelveny.sz4] = True
    kihuzott_szamok[szelveny.sz5] = True
for m in range(1, 91):
    if not kihuzott_szamok.get(m, False):
        van = True
        break
print("Van." if van else "Nincs.")
# 6. FELADAT
paratlan = 0
for szelveny in lottoszamok:
    if len([l for l in (szelveny.sz1, szelveny.sz2, szelveny.sz3, szelveny.sz4, szelveny.sz5) if l % 2 != 0]) > 0:
        paratlan += 1
print(paratlan)
# 7. FELADAT
with open("lotto52.ki", "w") as f:
    for szelveny in lottoszamok:
        print(f"{szelveny.sz1} {szelveny.sz2} {szelveny.sz3} {szelveny.sz4} {szelveny.sz5}", file=f)
    print(f"{szamok[0]} {szamok[1]} {szamok[2]} {szamok[3]} {szamok[4]}", file=f)
# 8. FELADAT
uj_lottoszamok = beolvas("lotto52.ki")
kihuzott_szamok_szama = {}
with open("lotto52.ki", "r") as f:
    for szelveny in uj_lottoszamok:
        kihuzott_szamok_szama[szelveny.sz1] = kihuzott_szamok_szama.get(szelveny.sz1, 0) + 1
        kihuzott_szamok_szama[szelveny.sz2] = kihuzott_szamok_szama.get(szelveny.sz2, 0) + 1
        kihuzott_szamok_szama[szelveny.sz3] = kihuzott_szamok_szama.get(szelveny.sz3, 0) + 1
        kihuzott_szamok_szama[szelveny.sz4] = kihuzott_szamok_szama.get(szelveny.sz4, 0) + 1
        kihuzott_szamok_szama[szelveny.sz5] = kihuzott_szamok_szama.get(szelveny.sz5, 0) + 1
for m in range(1, 91):
    print(kihuzott_szamok_szama.get(m, 0), end=' ')
print()
# 9. FELADAT
primszamok = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
kihuzott_primek = set()
#lottoszamok.pop()
for szelveny in lottoszamok:
    #print(szelveny.sz1, szelveny.sz2, szelveny.sz3, szelveny.sz4, szelveny.sz5)
    for l in (szelveny.sz1, szelveny.sz2, szelveny.sz3, szelveny.sz4, szelveny.sz5):
        if l in primszamok:
            kihuzott_primek.add(l)
print("A következő prímszámokat egyszer sem húzták ki: ", end="")
for prim in primszamok:
    if prim not in kihuzott_primek:
        print(prim, end=" ")


