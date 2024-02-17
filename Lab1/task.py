def print_info(r1,r2,s1,s2,t1,t2,iter):
    print("Итерация №",iter," \n r1 = ", r1," r2 = ",r2,
          " s1 = ",s1," s2 = ",s2," t1 = ",t1," t2 = ",t2)

def Evklid(r1,r2,s1,s2,t1,t2, iter):
    print_info(r1,r2,s1,s2,t1,t2, iter)
    q = r1//r2
    r = r1 - q*r2
    if r == 0:
        s = s1 - q * s2
        t = t1 - q * t2
        print_info(r2,r,s2,s,t2,t, iter+1)
        return s2, t2, s2*a+t2*b
    else:
        s = s1 - q*s2
        t = t1 - q*t2

        return Evklid(r2,r,s2,s,t2,t, iter+1)

def start_Evklid(r1, r2, m):
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    iter = 0
    s, t, d = Evklid(r1, r2, s1, s2, t1, t2, iter)

    print("Полученные значения s,t и d\n", a, t, d)
    print("Полученное выражение:")
    print(a, "*", s, "+", b, "*", t, " = ", d)

    if m%d !=0:
        return None
    else:
        s = s*(m//d)
        t = t*(m//d)
        solutions = []
        for i in range(d):
            solution = s + i*m
            if solution >= 0:
                solutions.append(solution % b)
            else:
                while solution<0:
                    solution = solution+b
                solutions.append(solution)
        return solutions




a = int(input("Введите коэффициент a в сравнении (ax ≡ m (mod b)): "))
b = int(input("Введите коэффициент b в сравнении (ax ≡ m (mod b)): "))
m = int(input("Введите модуль m в сравнении (ax ≡ m (mod b)): "))
print("Введённое сравнение первой степени:\n ",a,'x = ',m," mod ",b)

solutions = start_Evklid(a, b, m)
if solutions is None:
    print("Сравнение не имеет решений.")
else:
    print("Решения сравнения", a, "x ≡", m, "(mod", b, "):")
    for solution in solutions:
        print("x =", solution)

