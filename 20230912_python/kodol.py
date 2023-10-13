def atalakit(szoveg):
    ekezet = {"á": "a", "é": "e", "í": "i", "ó": "o", "ö": "o", "ő": "o", "ú": "u", "ü": "u", "ű": "u"}
    ret = ""
    for c in szoveg.lower():
        if c.isalpha():
            ret += ekezet.get(c, c)
    return ret.upper()

def beolvas():
    with open("vtabla.dat", "r") as f:
        ret = [line.strip() for line in f]
    return ret

jo_szoveg = False
while not jo_szoveg:
    nyilt_szoveg = input("Kérek egy maximum 255 karakterből álló szöveget: ")
    jo_szoveg = len(nyilt_szoveg) > 0

if len(nyilt_szoveg) > 255:
    nyilt_szoveg = nyilt_szoveg[:255]

nyilt_szoveg = atalakit(nyilt_szoveg)
print(f"Átalakított szöveg: {nyilt_szoveg}")

jo_szoveg = False
while not jo_szoveg:
    kulcsszo = input("Kérek egy kulcsszót (nincs benne ékezet): ")
    jo_szoveg = len(kulcsszo) > 0

if len(kulcsszo) > 5:
    kulcsszo = kulcsszo[:5]

kulcsszo = kulcsszo.upper()
#print(kulcsszo)
kulcsszoveg = ""
while len(kulcsszoveg) + len(kulcsszo) <= len(nyilt_szoveg):
    kulcsszoveg += kulcsszo

if len(kulcsszoveg) < len(nyilt_szoveg):
    kulcsszoveg += kulcsszo[:len(nyilt_szoveg) - len(kulcsszoveg)]

print(f"Létrehozott kulcsszöveg: {kulcsszoveg}")
tabla = beolvas()
#for sor in tabla:
#    print(sor)
kodolt_szoveg = ""
for i, j in zip(nyilt_szoveg, kulcsszoveg):
    kodolt_szoveg += tabla[ord(i) - ord("A")][ord(j) - ord("A")]

print(f"A kódolt syöveg: {kodolt_szoveg}")
with open("kodolt.dat", "w") as f:
    print(kodolt_szoveg, file=f)