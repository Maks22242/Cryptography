import hashlib


def calculate_sha256(text):
    # Преобразование текста в байты (UTF-8 кодировка)
    encoded_text = text.encode('utf-8')

    # Создание объекта хеша SHA-256
    sha256_hash = hashlib.sha256()

    # Обновление объекта хеша с данными
    sha256_hash.update(encoded_text)

    # Получение и возврат итогового хеша в шестнадцатеричном формате
    return sha256_hash.hexdigest()


if __name__ == "__main__":
    # Ввод текста от пользователя
    text = input("Введите текст для вычисления SHA-256 хеша: ")

    # Вычисление SHA-256 хеша для введенного текста
    sha256_hash = calculate_sha256(text)

    # Вывод результата
    print("SHA-256 хеш для введенного текста:", sha256_hash)
