# 1. feladat
import string

class Maganhangzok:
    def __init__(self, szoveg, betuk):
        self.szoveg = szoveg
        self.betuk = betuk
    def betu_szam(self):
        betuk = set(self.betuk)
        ret = 0
        for char in self.szoveg:
            if char in betuk:
                ret += 1
        return ret
    def statisztika(self):
        betuk = {c: 0 for c in self.betuk}
        for char in self.szoveg:
            if betuk.get(char) is not None:
                betuk[char] += 1
        return dict(sorted(list(betuk.items()), key=lambda n: n[1], reverse=True))

class Massalhangzok(Maganhangzok):
    def __init__(self, szoveg, betuk):
        super().__init__(szoveg, betuk)

s = input("Kérek egy szöveget! ").lower()
mgh = Maganhangzok(s, {'a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű'})
print(mgh.betu_szam())
print(mgh.statisztika())
msh = Massalhangzok(s, set(string.ascii_lowercase).difference({'a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű'}))
print(msh.betu_szam())
print(msh.statisztika())

# 2. feladat
class Simple:
    probaszam = 3
    def __init__(self, sorszam, pin):
        self.sorszam = sorszam
        self.pin = pin
        self.aktivalva = False
        self.ervenytelen = False
        self.proba = 0
        self.egyenleg = 0
    def aktival(self, pin):
        if self.ervenytelen or self.aktivalva: return
        if pin != self.pin:
            self.proba += 1
            if self.proba >= self.probaszam:
                self.ervenytelen = True
        elif self.proba < self.probaszam:
            self.aktivalva = True

class Improved(Simple):
    def __init__(self, sorszam, pin, puk):
        super().__init__(sorszam, pin)
        self.puk = puk
    def ujraaktival(self, puk):
        if not self.ervenytelen or self.aktivalva: return
        if puk == self.puk:
            self.ervenytelen = False
            self.aktivalva = True

class KartyaKezelo:
    def __init__(self):
        self.kartyak = []
    def kartya_letrehoz(self):
        sorszam = int(input("Kérem a SIM kártya sorszámát! "))
        pin = int(input("Kérem a SIM kártya PIN kódját! "))
        puk = int(input("Kérem a SIM kártya PUK kódját! "))
        self.kartyak.append(Improved(sorszam, pin, puk))
    def kartya_keres(self, sorszam):
        try:
            kartya = next(filter(lambda n: n.sorszam == sorszam, self.kartyak))
        except StopIteration:
            return None
        return kartya
    def kartya_aktival(self):
        kartya = self.kartya_keres(int(input("Kérem a SIM kártya sorszámát! ")))
        if kartya is None:
            print("Nincs ilyen SIM kártya!")
        elif kartya.aktivalva:
            print("Ez a kártya már aktiválva van!")
        elif kartya.ervenytelen:
            while not kartya.aktivalva:
                puk = input("Kérem a PUK-kódot, vagy egy '.'-t a kilépéshez! ")
                if puk == '.': return
                kartya.ujraaktival(int(puk))
                if kartya.aktivalva:
                    print("A kártya aktiválva van!")
        else:
            while not kartya.aktivalva and not kartya.ervenytelen:
                pin = input(f"Kérem a PIN-kódot ({kartya.probaszam - kartya.proba} próbálkozás maradt), vagy egy '.'-t a kilépéshez! ")
                if pin == '.': return
                kartya.aktival(int(pin))
            if kartya.ervenytelen:
                print("A kártya érvénytelenítve lett! Újraérvényesítéshez használja a PUK-kódot!")
            elif kartya.aktivalva:
                print("A kártya aktiválva van!")
    def kartya_egyenleg(self):
        kartya = self.kartya_keres(int(input("Kérem a SIM kártya sorszámát! ")))
        if kartya is None:
            print("Nincs ilyen SIM kártya!")
        else:
            print(f"A kártya jelenlegi egyenlege: {kartya.egyenleg}.")
            add = int(input("Mennyivel szeretné változtatni a kártya egyenlegét? "))
            kartya.egyenleg += add
            print(f"A kártya új egyenlege: {kartya.egyenleg}.")
        
kezelo = KartyaKezelo()
option = input("Válasszon az alábbiak közül: kártya (l)étrehozása, (a)ktiválása, (e)gyenleg, (v)ége! ").lower()
while option != 'v':
    option = option.lower()
    if option == 'l':
        kezelo.kartya_letrehoz()
    elif option == 'a':
        kezelo.kartya_aktival()
    elif option == 'e':
        kezelo.kartya_egyenleg()
    option = input("Válasszon az alábbiak közül: kártya (l)étrehozása, (a)ktiválása, (e)gyenleg, (v)ége! ").lower()

# 3. feladat
class Hatvany:
    def __init__(self, alap, kitevo):
        if alap < 0:
            print("Az alap nem lehet negatív!")
            return
        self.alap = alap
        self.kitevo = self.kerekit(abs(kitevo)) * ((kitevo > 0) - (kitevo < 0))
        self.hatvany = self.hatvanyoz(self.alap, self.kitevo)
    def kerekit(self, kitevo):
        print("A kitevő kerekítve lesz!")
        egesz = kitevo - int(kitevo)
        szamjegy = int(egesz * 10)
        if szamjegy < 5:
            return int(kitevo)
        elif szamjegy > 5:
            return int(kitevo) + 1
        return kitevo
    def hatvanyoz_base(self, a, b):
        if b <= 0:
            return 1
        return self.hatvanyoz_base(a, b-1) * a
    def hatvanyoz(self, a, b):
        if b < 0:
            return 1 / self.hatvanyoz_base(a, -b)
        elif b >= 0:
            return self.hatvanyoz_base(a, b)

def sign(n):
    return (n > 0) - (n < 0)

class Gyok(Hatvany):
    def __init__(self, alap, kitevo):
        if int(kitevo * 10) % 10 == 5: 
            szamlalo, nevezo = self.koz_tort(kitevo)
            super().__init__(alap, szamlalo)
            self.hatvany = self.hatvanyoz(self.alap, self.kitevo)
        else:
            super().__init__(alap, kitevo)
        if int(kitevo * 10) % 10 == 5:
            self.gyok = self.gyokot_von(self.hatvany)
    def gcd(self, a, b):
        s_a, s_b = sign(a), sign(b)
        a, b = abs(a), abs(b)
        if a == b:
            return (a + b) // 2
        if a > b:
            a -= b
        else:
            b -= a
        return self.gcd(a * s_a, b * s_b)
    def koz_tort(self, n):
        if int(n * 10) % 10 == 5:
            gcd = self.gcd(int(n * 10), 10)
            szamlalo, nevezo = (n * 10) // gcd, 10 // gcd
            return szamlalo, nevezo
    def gyokot_von(self, n):
        x = 1
        for i in range(1000):
            x = 0.5*(x + n/x)
        return x
    def kerekit(self, kitevo):
        print("A kitevő kerekítve lesz!")
        tort = kitevo - int(kitevo)
        egesz = int(kitevo)
        elso, masodik = divmod(tort * 100, 10)
        if elso == 5:
            return egesz + 0.5
        elif elso == 4:
            return egesz + 0.5
        elif elso == 3:
            if masodik >= 5:
                return egesz + 0.5
            else:
                return egesz
        elif elso == 6:
            return egesz + 0.5
        elif elso == 7:
            if masodik < 5:
                return egesz + 0.5
            else:
                return egesz + 1
        elif elso <= 2:
            return egesz
        elif elso >= 8:
            return egesz + 1

hatvany = Hatvany(4, 2)
print(hatvany.hatvany)

gyok = Gyok(4, 2.5)
print(gyok.gyok)
