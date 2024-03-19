def gf2_add(a, b):
    """Сложение многочленов в поле GF(2)"""
    return a ^ b

def gf2_sub(a, b):
    """Вычитание многочленов в поле GF(2)"""
    return a ^ b

def gf2_mul(a, b):
    """Умножение многочленов в поле GF(2)"""
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11B # x^8 + x^4 + x^3 + x + 1 (примитивный многочлен)
        b >>= 1
    return result

def gf2_degree(poly):
    """Нахождение степени многочлена"""
    degree = -1
    while poly:
        degree += 1
        poly >>= 1
    return degree

def gf2_gcd(a, b):
    """Нахождение наибольшего общего делителя многочленов"""
    while b:
        a, b = b, a % b
    return a

def is_primitive(poly):
    """Проверка многочлена на примитивность"""
    n = gf2_degree(poly)
    for i in range(1, n):
        if gf2_gcd(poly, (1 << n) - 1) == 1:
            if gf2_degree(gf2_mul(poly, poly)) == n:
                return True
            else:
                return False
    return False

def is_irreducible(poly):
    """Проверка многочлена на неприводимость"""
    for i in range(1, gf2_degree(poly) // 2 + 1):
        if gf2_gcd(poly, (1 << (2 ** i)) + 1) != 1:
            return False
    return True

#Пример многочлена 0b100011011
poly = int(input("Введите многочлен в двоичной форме: "), 2)

if is_irreducible(poly):
    print("Многочлен является неприводимым")
else:
    print("Многочлен не является неприводимым")

if is_primitive(poly):
    print("Многочлен является примитивным")
else:
    print("Многочлен не является примитивным")

