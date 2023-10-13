# alap-rekurziók
# Fibonacci sorozat. a1 = 0, a2 = 1, an = an-2 + an-1
#
#        | n = 0, akkor 0
# F(n) = | n = 1, akkor 1
#        | n > 1, akkor F(n-1) + f(n-2)
#
# Algorimus Fibonacci(egész: n): egész
# Algoritmus kezdete
#   Ha n = 0 akkor Fibonacci = 0
#   Különben Ha n = 1 akkor Fibonacci = 1
#   Különben Fibonacci = Fibonacci(n-1) + Fibonacci(n-2)
#   Elágazás vége
# Algoritmus vége
#
# ----------------------------------------------------------------------
#
# FAKTORIÁLIS
# n! = n*(n-1)*(n-2)*...*1
# Definíció szerint 0! = 1
#
# Fakt(n) = | n = 0, akkor 1
#           | n > 0, akkor n*Fakt(n-1)
# 
# Algoritmus Fakt(egész: n): egész
# Algoritmus kezdete
#   Ha n = 0 akkor Fakt = 1
#   Különben Fakt = n * Fakt(n-1)
# Algoritmus vége
#
# ---------------------------------------------------------------------
#
# BINÁRIS VÁLTÓ
# 
# Bin(n) = | n = 0, akkor üres string
#          | n > 0, akkor Bin(n // 2) + str(n % 2)
# 
# --------------------------------------------------------------------
#
# BINOMIÁLIS EGYÜTTHATÓK
#
# (a+b)^0         1
# (a+b)^1        1 1
# (a+b)^2       1 2 1
# (a+b)^3      1 3 3 1           a^4        a^3 b    a^2 b^2      a b^3      b^4
# (a+b)^4     1 4 6 4 1     -> a^4 b^0 -> a^3 b^1 -> a^2 b^2 -> a^1 b^3 -> a^0 b^4
#
# Binom(k, n) = | k = 0, vagy k = n, akkor 1
#               | 0 < k < n, akkor Binom(k-1, n-1) + Binom(k, n-1)
#
# Algoritmus Binomialis(egész: k, egész: n): egész
# Algoritmus kezdete
#   Ha k = 0 vagy k = n akkor Binomialis = 1
#   Különben Binomialis = Binomialis(k-1, n-1) + Binomialis(k, n-1)
#   Elágazás vége
# Algoritmus vége
#
# HF: 
# 1. A Fibonacci sorozatot oldd meg NEM rekurzív módon ciklus(ok) használatával.
# 2. A Binomiális együtthatók feladatot dolgozd át úgy, hogy a változók is ki legyenek írva!
#    (a+b)^3 = 1*a^3*b^0 + 3*a^2*b^1 + 3*a^1*b^2 + 1*a^0*b^3
def fibonacci(n): # n - hanyadik Fibonacci számot keressük
    if n <= 1:
        return n
    k = fibonacci(n-2) + fibonacci(n-1)
    return k

def fakt(n):
    if n == 0:
        return 1
    k = n * fakt(n-1)
    return k

def dec2bin(n):
    if n == 0:
        return ""
    return dec2bin(n // 2) + str(n % 2)

def binomialis(k, n):
    if k == 0 or k == n:
        return 1
    return binomialis(k-1, n-1) + binomialis(k, n-1)

def fibonacci2(n):
    if n <= 1:
        return n
    elso = 0
    masodik = 1
    for _ in range(n-1):
        szum = elso + masodik
        elso = masodik
        masodik = szum
    return szum

# FŐPROGRAM
n = int(input("Hányadik Fibonacci számot keressük? "))
print(fibonacci(n-1))
print(fibonacci2(n-1))

n = int(input("Melyik szám faktoriálisát keressük? "))
if n >= 0:
    print(f"{n}! = {fakt(n)}")

n = int(input("Melyik számot akarjuk binárissá alakítani? "))
print(dec2bin(n))

n = int(input("Kérem a fokszámot! "))
a = n
b = 0
for i in range(n+1):
    #print(binomialis(i, n), end=' ')
    print(f"{binomialis(i, n)}*a^{a}*b^{b}", end=' + ' if i < n else '')
    a -= 1
    b += 1
