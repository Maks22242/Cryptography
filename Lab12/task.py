from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
import os

"""
Генерируем ключевую пару (приватный и публичный ключи).
Подписываем файл с использованием приватного ключа.
Проверяем подпись файла с использованием публичного ключа.
"""

def generate_keypair():
    private_key = dsa.generate_private_key(key_size=1024, backend=default_backend())
    public_key = private_key.public_key()
    return private_key, public_key


def sign_file(private_key, file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    signature = private_key.sign(data, hashes.SHA256())
    return signature


def verify_signature(public_key, file_path, signature):
    with open(file_path, 'rb') as file:
        data = file.read()
    try:
        public_key.verify(signature, data, hashes.SHA256())
        print("Подпись верна.")
    except:
        print("Подпись не верна.")


if __name__ == "__main__":
    # Генерация ключевой пары
    private_key, public_key = generate_keypair()

    # Подписывание файла
    file_to_sign = "example.txt"
    signature = sign_file(private_key, file_to_sign)

    # Проверка подписи
    verify_signature(public_key, file_to_sign, signature)
