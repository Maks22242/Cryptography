#Проверка числа на простоту
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def find_quadratic_residues_nonresidues(p):
    residues = []
    nonresidues = []

    for a in range(1, p):
        residue = (a ** 2) % p
        if residue not in residues:
            residues.append(residue)

    for b in range(1, p):
        if b not in residues:
            nonresidues.append(b)

    return residues, nonresidues

def info(p):
    print("Система вычетов по модулю ",p,"состоит из ",int((p-1)/2)," Квадратичных вычетов\n и ",int((p-1)/2)," квадратичных невычетов")
p = 13  # Простое число
if is_prime(p):
    info(p)
    quadratic_residues, quadratic_nonresidues = find_quadratic_residues_nonresidues(p)

    print(f"Множество квадратичных вычетов по модулю {p}: {quadratic_residues}")
    print(f"Множество квадратичных невычетов по модулю {p}: {quadratic_nonresidues}")
else:
    print("Введённое число не является простым")
