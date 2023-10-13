class Osztaly:
    valtozo = 1 # public változó
    _valtozo = 2 # protected változó
    __valtozo = 3 # private változó
    def __init__(self, valtozo):
        self.valtozo = valtozo # ez a sor override a "valtozo" attribútumhoz!!
    def metodus(self):
        #self.valtozo = "anyu"
        return self.valtozo
    def privat_proba(self):
        return self.__valtozo * 10

class Orokos(Osztaly):
    """
    def __init__(self, vvv):
        self.V = vvv
    """
    def nyomtat(self):
        #return self.V
        #a = self.__valtozo # erre hibát ad a Python
        return self.valtozo

Or = Orokos("$$$")
print(Or.valtozo)
print(Or._valtozo)
print(Or.metodus())
print(Or.nyomtat())
print(Or.privat_proba())
"""
O = Osztaly("hahó")
print(O.valtozo)
print(O._valtozo)
#print(O.__valtozo)
print(O.metodus())
"""
# Készíts egy "kor" osztályt, mely paraméterül a kör sugarát kapja! Két public attribútumban
# (változóban) add vissza a kör kerületét és területét!
# Készíts örököst a "kor" osztályhoz, "gomb" néven! A "gomb" osztály adja vissza a gömb
# legnagyobb kerületét, a gömbközéppontban átmenő metszet területét, valamint a gömb
# felszínét és térfogatát!
import math
class Kor:
    def __init__(self, r):
        self.kerulet = 2 * r * math.pi
        self.terulet = r * r * math.pi

class Gomb(Kor):
    def __init__(self, r):
        super().__init__(r)
        self.felszin = 4 * r * r * math.pi
        self.terfogat = 4 * r * r * r * math.pi / 3

k = Kor(5)
print(k.kerulet)
print(k.terulet)
print()
g = Gomb(5)
print(g.kerulet)
print(g.terulet)
print(g.felszin)
print(g.terfogat)
