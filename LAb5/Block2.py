import math
import sympy

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def f(x):
    return x**2+1

def pollard_p1(n,B):
    # n - раскладываемое число
    a = 2
    e = 2
    while (e<=B):
        a = a**e % n
        e +=1
    p = gcd(a-1,n)
    if 1<p and p<n:
        return p
    return 0

def PO(n,B):
    x= 2
    y =2
    p = 1
    while p == 1:
        x = f(x)%n
        y = f(f(y)%n)%n
        p = gcd(x - y,n)
    return p
# Квадратичное решето
def quadratic_sieve(N):
    a = math.isqrt(N) + 1
    while True:
        b_squared = a**2 - N
        b = math.isqrt(b_squared)
        if b**2 == b_squared:
            k = a + b
            factor = math.gcd(k, N)
            if factor != 1 and factor != N:
                return factor, N // factor
        a += 1
#Решето поля чисел

def quadratic_sieve_field(N):
    for d in [-1, -2, -3, -7, -11]:
        if pow(d, (N - 1) // 2, N) == N - 1:
            break
    else:
        raise ValueError("Не удалось найти квадратичное невычетное d")

    Q = sympy.QQ.algebraic_field(sympy.sqrt(d))
    N = Q(N)
    factors = []
    for p in sympy.primerange(2, sympy.isqrt(N) + 1):
        if N % p == 0:
            factors.append(p)
            while N % p == 0:
                N //= p
        if N == 1:
            break
    if N > 1:
        factors.append(N)
    return factors

#квадратичное поле чисел
def prime_factors(n):
    # Инициализация списка простых множителей
    prime_factors_list = []

    # Находим все простые числа до корня из n
    primes = []
    sieve = [True] * (int(n ** 0.5) + 1)
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, int(n ** 0.5) + 1, p):
                sieve[i] = False

    # Находим простые множители числа n
    for prime in primes:
        while n % prime == 0:
            prime_factors_list.append(prime)
            n //= prime
        if n == 1:
            break

    # Если после деления осталось число больше 1, то оно тоже простое
    if n > 1:
        prime_factors_list.append(n)

    return prime_factors_list

def tasks(n):
    print("Введённое число: ", n )
    B = 8
    p = pollard_p1(n,B)
    k = n /p
    print("№7) p – 1 Метод Полларда при В = ",B,"\n", n ," = ",p," * ",k)
    p = PO(n,B)
    k = n / p
    print("№8) РО (Rho) – метод Полларда при В = ", B, "\n", n, " = ", p, " * ", k)
    p, k = quadratic_sieve(n)
    print("№9) квадратичное решето разложения на множители – метод Полларда \n", n, " = ", p, " * ", k)
    p = prime_factors(n)
    print("№10) решето поля чисел разложения на множители - Решето Эратосфена \n", n, " = ", p)


n = 483
tasks(n)