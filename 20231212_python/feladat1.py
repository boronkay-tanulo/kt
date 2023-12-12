def haromra_vag(s):
    s_len = len(s)
    egy_hossz = s_len // 3
    hatar1, hatar2 = egy_hossz * 1, egy_hossz * 2
    e, k, v = s[:hatar1], s[hatar1:hatar2], s[hatar2:]
    return k+v+e

mondat = input("Kérek egy mondatot! ")
print("A felcserélt mondat:", haromra_vag(mondat))
