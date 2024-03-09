import random
def general(vnev, knev):
    return vnev[:3].upper() + "_" + knev[-2:] + str(random.randint(10, 99))

print("2. feladat")
vnev = input("Kérem adja meg a vezetéknevét:\n")
knev = input("Kérem adja meg a keresztnevét:\n")
print("Felhasználónév:", general(vnev, knev))
