jaratok = []
for i in range(3):
    with open(f"jarat{i+1}.txt", "r", encoding="utf-8") as f:
        jaratok.append(set(f.read().splitlines()))
print(f"Járat 1 -> Járat 2: {jaratok[0].intersection(jaratok[1])}")
print(f"Járat 2 -> Járat 3: {jaratok[1].intersection(jaratok[2])}")
print(f"Járat 1 -> Járat 3: {jaratok[0].intersection(jaratok[2])}")