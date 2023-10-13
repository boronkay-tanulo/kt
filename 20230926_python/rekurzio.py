# Rekurzió
# A rekurzió gondolat olyan feladat megfogalmazás, melyben egy metódust átparaméterezve addig
# hívunk újra meg újra, amíg a kilépési feltételt el nem érjük.
# A rekurzióban a METHOD() metódust meghívásának helye a METHOD() metódus!
# A rekurzív metódusok ezek alapján saját magukat hívják meg. a hívásnál új paramétereket
# adnak át, akkor globális paramétereket kell használni.
# A rekurzió a ciklust váltja ki. A legtöbb rekurzióban ezért nem található ciklus! (Létezik kivétel!)
# Előnye, hogy rövid, elegáns kódokat tudunk létrehozni. Hátránya, hogy - sok hívás esetén -, megzabálja a
# memóriát. Amennyiben számokat keresünk rekurzívan, figyelni kell a tárolási méretekre is, mert hamar ki
# tudunk lépni egy-egy változó maximális méretéből.
# A rekurzió több modellel is leírható. Amennyiben a rekurzív metódus egy függvény, a pince modell a
# legjobb leírója: elindulunk lefele egy pince lépcsőjén, és minden lépcsőn hagyunk egy kannát.
# Amikor elérjük a kilépési feltételt (pl. a pincét), a legalsó kannában lévő folyadékot beletöltjük
# az előző lépcsőn lévő kannába. Mire felérünk a pincéből, minden kanna tartalma valamely mértékben
# megváltozott. Ebben az esetben viszont, csak a felső kanna tartalma a számunkra érdekes.
# Amenyiben a rekurziv metódus egy eljárás, akkor nincs visszafele lépegetés. Ilyenkor a kilépési
# feltétel bekövetkeztekor érvényben lévő változó-tartalmakat keressük.
#
# Programozási taktika
#   1. Az eredeti problémát az eredetivel megegyező (nagyon hasonló) részproblémákra
#      bontjuk, mindaddig amíg az alapesetet el nem érjük.
#   2. A részproblémák megoldásait összekapcsoljuk
#      a. minden rekurzív definíciónak van egy, vagy több alapesete, melyeknek triviális
#         megoldása van. pl. rekurzív hatványozás: n^k - ha k = 0 return 1
#                        pl. rekurzív faktoriális: n! - ha n = 0 return 1
#      b. minden rekurzív definíciónak van egy, vagy több rekurzív esete, mikor a függvény
#         új paraméterekkel meghívja saját magát.
#
# A rekurzió típusai:
#   1. Hívások száma (a kódon belül) alapján:
#      a. egyszeres rekurzió, mely csak egy hívást tartalmaz
#      b. többszörös, mikor önmagát többféleképpen paraméterezve hívhatja meg
#   2. a hívott függvény szerint:
#      a. közvetlen rekurzió, mikor a fv. saját magát hívja
#      b. közvetett rekurzió, mikor f => g, majd g => f módón valósul meg a hívás
#   3. Nevesítés szerint:
#      a. névvel ellátott rekurzió
#      b. névtelen (lambda) rekurzió
#
# REKURZÍV ADATTÍPUSOK
# Amikor egy program előre nem látható mennyiségű adatot produkál, a programozó rekurzív módon
# definiálhatja az adatszerkezetet. Ezt kétféleképpen lehet megtenni, induktív vagy koinduktív módon.
# Tipikus induktív adathalmaz pl. a N - természetes számok halmaza:
#   Definíciója: Egy természetes szám vagy 0, vagy n+1 alakú, ahol n egy természetes szám.
# Hasonló a láncolt lista:
# class Csomópont:
#   következőCsomópont = null
#   //mit tárolunk ezen a csomóponton:
#   objektum
# A fenti példából kihagytam a sallangokat :).
#
# Példa egy koinduktív adathalmaz definícióra:
# "Egy string-lánc egy objektum, ahol:
#   EGY_betu - egy darab (elemű) string
#   TOBBI_betu - egy "string-lánc"
# Hasonlít az indukívra, de ez pontosan meghatározza, hogy miként megy a feltöltése a string-láncnak.
def szorzas_rekurzio(a, b):
    if b == 0:
        return 0
    else:
        return szorzas_rekurzio(a, b-1) + a

def hatvany_rekurzio(a, b):
    if b == 0:
        return 1
    else:
        return hatvany_rekurzio(a, b-1) * a

# FŐPROGRAM
print(hatvany_rekurzio(3, 500))
