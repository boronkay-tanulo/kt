import random

class Keno:
    def __init__(self, tippek, huzas_szam):
        self.tipp_l = tippek
        self.huzasn = huzas_szam
        self.tipp_num = len(tippek)
    def huzas(self):
        ret = set()
        for n in range(20):
            jo_szam = False
            while not jo_szam:
                uj_szam = random.randint(1, 80)
                jo_szam = uj_szam not in ret
                if jo_szam: ret.add(uj_szam)
        return ret
    def full_talalat(self, kihuzottak):
        num = 0
        for tipp in self.tipp_l:
            if tipp in kihuzottak:
                num += 1
        return num == self.tipp_num
    def teszt(self):
        talalatok = 0
        for k in range(self.huzasn):
            #h = self.huzas()
            jo_talalat = self.full_talalat(self.huzas())
            if jo_talalat: talalatok += 1
            #print(h)
        return talalatok

print("Keno tesztelő alkalmazás")

jo_szamok_szama = False
while not jo_szamok_szama:
    szamok_szama = int(input("Hány számot szeretne megjelölni? 1-10 közötti egész számot kérek! "))
    jo_szamok_szama = (1 <= szamok_szama <= 10)

tippek = []
for i in range(szamok_szama):
    jo_tipp = False
    while not jo_tipp:
        tipp = int(input("Kérem a következő tippet! 1-80 közötti egész számot kérek! "))
        jo_tipp = (1 <= tipp <= 80 and tipp not in tippek)
        if jo_tipp: tippek.append(tipp)

tippek.sort()
jo_huzas = False
while not jo_huzas:
    huzas_szam = int(input("Kérem a húzások számát! 1-1700000000000 közötti egész számot kérek! "))
    jo_huzas = (1 <= huzas_szam <= 1700000000000)

keno = Keno(tippek, huzas_szam)
talalat_szam = keno.teszt()
print(talalat_szam)
