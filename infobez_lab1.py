import random
import string

# создание строки допустимых символов
rus_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.upper()
alphabet = string.ascii_letters + string.digits + string.punctuation + rus_alph

print("Допустимые символы для пароля", alphabet, sep="\n\n")

# функция генерации для паролей
def generate_password(alphabet, length=8):
    return ''.join(random.choice(alphabet) for i in range(length))

# генерация паролей и их запись в файл
with open('passwords.txt', 'w') as file:
    passwords = [generate_password(alphabet) for _ in range(20)]
    file.write('\n'.join(passwords))

print("\nФайл passwords.txt, содержащий 20 восьмисимвольных паролей сгенерирован.")
