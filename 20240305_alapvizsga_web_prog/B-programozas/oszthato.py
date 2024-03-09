print("1. feladat")
for i in range(50, 197):
    if i % 4 == 0 and i % 7 == 0:
        print(i, end="," if i < 196 else "")