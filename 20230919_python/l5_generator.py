import random
# számok bekérése, vizsgáljuk, hogy mindegyik különböző
# húzások számának bekérése, vizsgáljuk, hogy + egész legyen, max. 50000000
# húzások elvégzése, minden esetben 5 különböző szám kell!
# húzások összehasonlítása a tippel, a találatok lejegyzése
class L5:
    def __init__(self, tipp_list, huzas_szam):
        self.tl = tipp_list
        self.hsz = huzas_szam
    def egyhuzas(self):
        kihuzottak = []
        for i in range(5):
            jo_szam = False
            while not jo_szam:
                szam = random.randint(1, 90)
                if szam not in kihuzottak:
                    kihuzottak.append(szam)
                    jo_szam = True
        return kihuzottak
    def talalat_szam(self, kihuzottak):
        talalatok = 0
        for egy_tipp in self.tl:
            for szam in kihuzottak:
                if egy_tipp == szam:
                    talalatok += 1
        return talalatok
    def tesztel(self):
        eredmeny = {2: 0, 3: 0, 4: 0, 5: 0}
        for i in range(self.hsz):
            akt_huzas = self.egyhuzas()
            talalat_szam = self.talalat_szam(akt_huzas)
            if talalat_szam > 1:
                eredmeny[talalat_szam] += 1
        return eredmeny

# FŐPROGRAM
print("LOTTO5 tesztelő alkalmazás")
tippek = []
for i in range(5):
    tipp_rendben = False
    while not tipp_rendben:
        egy_tipp = int(input("Add meg a következő tippedet! 1-90 közötti egész számot kérek! "))
        if egy_tipp not in tippek and 1 <= egy_tipp <= 90:
            tippek.append(egy_tipp)
            tipp_rendben = True

tippek.sort()
huzasszam_rendben = False
while not huzasszam_rendben:
    huzas_szam = int(input("Kérem a húzások számát! 1-50000000 közötti egész szám! "))
    if 1 <= huzas_szam <= 50000000:
        huzasszam_rendben = True

peldany = L5(tippek, huzas_szam)
print(peldany.tesztel())
