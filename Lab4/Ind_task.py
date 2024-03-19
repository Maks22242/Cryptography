import random
import sympy

def out_privet_key(p,q):
    with open("private_key.txt", "w") as f:
        f.write(f"n: {p}\n")
        f.write(f"d: {q}")
def generate_keys():
    # Генерация двух простых чисел p и q
    p = sympy.randprime(10, 100)
    q = sympy.randprime(10, 100)



    # Вычисление модуля n
    n = p * q

    # Вычисление функции Эйлера от n
    phi = (p - 1) * (q - 1)

    # Выбор открытого ключа e
    e = random.randint(2, phi - 1)
    while sympy.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Вычисление закрытого ключа d
    d = sympy.mod_inverse(e, phi)
    out_privet_key(n, d)
    return ((n, e), (n, d))


def encrypt(message, public_key):
    n, e = public_key
    cipher_text = [pow(ord(char), e, n) for char in message]
    return cipher_text


def decrypt(cipher_text, private_key):
    n, d = private_key
    decrypted_text = [chr(pow(char, d, n)) for char in cipher_text]
    return ''.join(decrypted_text)


# Генерация ключей
public_key, private_key = generate_keys()
print("Открытый ключ:", public_key)
# print("Закрытый ключ:", private_key)

# Шифрование сообщения
message = "Whats going on?"
print("Исходное сообщение:", message)
cipher_text = encrypt(message, public_key)
print("Зашифрованное сообщение:", cipher_text)

# Расшифровка сообщения
decrypted_text = decrypt(cipher_text, private_key)
print("Расшифрованное сообщение:", decrypted_text)

