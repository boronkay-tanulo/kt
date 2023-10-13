class Aminosav:
    def __init__(self, rovidites, betujel, C, H, O, N, S):
        self.rovidites = rovidites
        self.betujel = betujel
        self.C = C
        self.H = H
        self.O = O
        self.N = N
        self.S = S
        self.tomeg = 0
    def tomeg_szamol(self):
        self.tomeg = C_TOMEG * self.C + H_TOMEG * self.H + O_TOMEG * self.O + N_TOMEG * self.N + S_TOMEG * self.S
    def __repr__(self):
        return f"Aminosav({self.rovidites}, {self.betujel}, {self.C}, {self.H}, {self.O}, {self.N}, {self.S}, {self.tomeg})"

C_TOMEG = 12
H_TOMEG = 1
O_TOMEG = 16
N_TOMEG = 14
S_TOMEG = 32

def to_dict(aminosavak):
    d = {}
    for aminosav in aminosavak:
        d[aminosav.betujel] = aminosav
    return d

def feladat1():
    aminosavak = []
    with open("aminosav.txt", "r") as f:
        for n, line in enumerate(f):
            if n % 7 == 0:
                l = []
            if n % 7 == 0 or n % 7 == 1:
                l.append(line.strip())
            else:
                l.append(int(line.strip()))
            if n % 7 == 6:
                aminosavak.append(Aminosav(*l))
    return aminosavak

def feladat2(aminosavak):
    for aminosav in aminosavak:
        aminosav.tomeg_szamol()

def feladat3(aminosavak):
    aminosavak.sort(key=lambda n: n.tomeg)
    print("3. feladat")
    with open("eredmeny.txt", "w") as f:
        print("3. feladat", file=f)
        for aminosav in aminosavak:
            s = f"{aminosav.rovidites} {aminosav.tomeg}"
            print(s, file=f)
            print(s)

def feladat4(aminosavak):
    lines = 0
    d = to_dict(aminosavak)
    ret = {"C": 0, "H": 0, "O": 0, "N": 0, "S": 0}
    with open("bsa.txt", "r") as f:
        for line in f:
            lines += 1
            ret["C"] += d[line.strip()].C
            ret["H"] += d[line.strip()].H - 2
            ret["O"] += d[line.strip()].O - 1
            ret["N"] += d[line.strip()].N
            ret["S"] += d[line.strip()].S
    with open("eredmeny.txt", "a") as f:
        print("4. feladat")
        print("4. feladat", file=f)
        for k, v in ret.items():
            print(f"{k} {v}", end=" ", file=f)
            print(f"{k} {v}", end=" ")
        print(file=f)
    print()

def feladat5():
    cur_len = 0
    max_len = 0
    print("5. feladat")
    with open("bsa.txt", "r") as f:
        content = f.read().strip().replace('\n', '')
        for idx, c in enumerate(content):
            #line = line.strip()
            cur_len += 1
            if c == "Y" or c == "W" or c == "F":
                if cur_len > max_len:
                    max_len = cur_len
                    start = idx - cur_len
                    end = idx
                    cur_len = 0
    with open("eredmeny.txt", "a") as f:
        print("5. feladat", file=f)
        s = f"leghosszabb darab hossza: {max_len - 1}; kezdete: {start + 1}; vége: {end + 1}"
        print(s, file=f)
        print(s)

def feladat6():
    buf = ""
    print("6. feladat")
    with open("bsa.txt", "r") as f:
        content = f.read().strip().replace('\n', '')
        for idx, c in enumerate(content):
            if c == "R" and content[idx+1] in {"A", "V"}:
                buf = content[:idx]
                break
    with open("eredmeny.txt", "a") as f:
        print("6. feladat", file=f)
        s = f"A BSA hasítása során keletkezett első fehérjelánc részletben {buf.count('C')} Cisztein található."
        print(s, file=f)
        print(s)

data = feladat1()
feladat2(data)
feladat3(data)
feladat4(data)
feladat5()
feladat6()
#print(data)
