import math

class Haromszog: # ez az ősosztály
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def szabalyos(self):
        return self.a == self.b == self.c
    def egyenloszaru(self):
        return self.a == self.b or self.a == self.c or self.b == self.c

class Szogek(Haromszog):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
    def derekszogu(self):
        an = self.a ** 2
        bn = self.b ** 2
        cn = self.c ** 2
        return an == bn + cn or bn == an + cn or cn == an + bn
    def hegyesszogu(self):
        an = self.a ** 2
        bn = self.b ** 2
        cn = self.c ** 2
        return an < bn + cn and bn < an + cn and cn < an + bn
    def tompaszogu(self):
        return not self.derekszogu() and not self.hegyesszogu()

# FŐPROGRAM
sz = Szogek(10, 10, 18)
print(f"Szabályos:    {sz.szabalyos()}")
print(f"Egyenlőszárú: {sz.egyenloszaru()}")
print(f"Derékszögű:   {sz.derekszogu()}")
print(f"Hegyesszögű:  {sz.hegyesszogu()}")
print(f"Tompaszögű:   {sz.tompaszogu()}")

