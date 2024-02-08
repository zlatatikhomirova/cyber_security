# кодовое слово
cyph_word = "ЭВДЕМОНИСТ"
# русский исходный алфавит
ru_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# алфавит шифрования
cyph_alphabet =  cyph_word + "".join(el for el in ru_alphabet if el not in cyph_word)
# с помощью str.maketrans получаем коды букв русского алфавита в обычном порядке и ставим им в соответствие коды букв из алфавита шифрования
cyph_table = str.maketrans(ru_alphabet, cyph_alphabet)

# получаем входную строку
s = input("Введите текст: ").upper()
# шифруем её
# str.translate(table) - символы в исходной строке меняет на соответствующие символы из cyph_table, применяя к кодам функцию chr - преобразование кода символа в символ
s_cyph = s.translate(cyph_table)
print("Зашифрованный текст", s_cyph)
