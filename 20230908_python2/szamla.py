from datetime import datetime, date
import math

class Hivas:
    def __init__(self, tel_szam, kezd_h, kezd_m, kezd_s, veg_h, veg_m, veg_s):
        self.tel_szam = tel_szam
        self.kezd = datetime.strptime(f"{kezd_h}:{kezd_m}:{kezd_s}", "%H:%M:%S")
        self.veg = datetime.strptime(f"{veg_h}:{veg_m}:{veg_s}", "%H:%M:%S")

data = []
with open("hivasok.txt", "r") as f:
    for i, line in enumerate(f):
        if i % 2 == 0:
            hivas_l = []
            for tmp in (int(i) for i in line.strip().split()):
                hivas_l.append(tmp)
        else:
            hivas_l.insert(0, int(line.strip()))
            data.append(Hivas(*hivas_l))

def mobil(n):
    n = str(n)
    return n.startswith("39") or n.startswith("41") or n.startswith("71")

def szamol_perc(hivas):
    percek = math.ceil((hivas.veg - hivas.kezd).total_seconds() / 60)
    return percek

def feladat1():
    szam = input("Kérek egy telefonszámot: ")
    if mobil(szam):
        print("A telefonszám mobil.")
    else:
        print("A telefonszám vezetékes.")

def feladat2():
    #k_ora, k_perc, k_mperc = (int(i) for i in input("Kérem a hívás kezdeti időpontját!(óra:perc:másodperc) ").split(':'))
    #v_ora, v_perc, v_mperc = (int(i) for i in input("Kérem a hívás végzésének időpontját!(óra:perc:másodperc) ").split(':'))
    kezd = datetime.strptime(input("Kérem a hívás kezdeti időpontját!(óra:perc:másodperc) "), "%H:%M:%S")
    veg = datetime.strptime(input("Kérem a hívás végzésének időpontját!(óra:perc:másodperc) "), "%H:%M:%S")
    ido = veg - kezd
    print(f"A hívás időtartama: {math.ceil(ido.total_seconds() / 60)} perc.")

def feladat3():
    with open("percek.txt", "w") as f:
        for hivas in data:
            percek = szamol_perc(hivas)
            print(f"{percek} {hivas.tel_szam}", file=f)

def feladat4():
    csucsido = 0
    kivul = 0
    for hivas in data:
        if 7 <= hivas.kezd.hour < 18:
            csucsido += 1
        else:
            kivul += 1
    print(f"Hívások csúcsidőn belül: {csucsido}.")
    print(f"Hívások csúcsidőn kívül: {kivul}.")

def feladat5():
    mobil_ = 0
    vezetekes = 0
    for hivas in data:
        percek = szamol_perc(hivas)
        if mobil(hivas.tel_szam):
            mobil_ += percek
        else:
            vezetekes += percek
    print(f"{mobil_} percet beszélt mobil számmal, és {vezetekes} percet beszélt vezetékessel.")

def feladat6():
    ossz = 0
    for hivas in data:
        percek = szamol_perc(hivas)
        if 7 <= hivas.kezd.hour < 18:
            ossz += (69.175 if mobil(hivas.tel_szam) else 30) * percek
    print(f"A csúcsdíjas hívásokért {ossz} Ft-t kell fizetni.")

def main():
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()

main()
