# выносим как константы алфавит и его размер
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPH_SIZE = len(alphabet)

# выносим как константы ключ и его длину, индексы которым соответствуют буквы в ключе
key = "VERA"
key_idx = tuple(alphabet.index(x) for x in key)
KEY_SIZE = len(key)

# если это не выполнится, то невозможно закодировать что-либо
# при данных параметрах
assert KEY_SIZE <= ALPH_SIZE, "KEY_SIZE > ALPH_SIZE"

# строим таблицу Виженера
table = [["" for i in range(ALPH_SIZE + 1)] for _ in range(ALPH_SIZE + 1)]
table[0] = [" "] + list(alphabet)
# заполняем её
for i in range(1, ALPH_SIZE + 1):
    table[i][0] = alphabet[i-1]
for i in range(1, ALPH_SIZE + 1):
    for j in range(1, ALPH_SIZE + 1):
        table[i][j] = alphabet[(j - 2 + i) % ALPH_SIZE]

def encode(text: str, de: bool = False, way: str = ''):
    # функция для кодирования строки с помощью таблицы Виженера
    # инициализация результирующей строки
    res = ""
    if way == 'table':
        # находим в таблице Виженера строку, соответствующую первому символу ключевого 
        # слова; столбец, в котором находится данный символ, соответствует первому 
        # символу исходного текста в данной позиции (строка, столбец) получаем первый
        # символ зашифрованного текста
        # следующие символы входного текста зашифровываются подобным образом
        code = lambda full_key_idx, text_idx: table[ full_key_idx + 1 ][ text_idx + 1 ]
    else:
        # функция для шифрования или дешифрования (если de=True) текста
        # с помощью формулы алгоритма шифрования Виженера
        # если нужно декодировать строку берем разность,
        # иначе сумму по алгоритму шифрования Виженера при помощи формулы
        # находим буквы в алфавите по индексу из формулы шифрования Виженера
        if de:
            code = lambda full_key_idx, text_idx: \
                             alphabet[ (text_idx - full_key_idx) % ALPH_SIZE ]
        else:
            code = lambda full_key_idx, text_idx: \
                             alphabet[ (text_idx + full_key_idx) % ALPH_SIZE ]
    j = 0 # переменная счетчик для прохода только по буквам входного текста
    # проходим по всем символам исходного текста
    for el in text:
        # если символ - буква, то кодируем его
        if el.isalpha():
            # находим индекс буквы входного текста в алфавите
            # для каждой буквы этого текста
            # тоже самое для циклоключа
            res += code(key_idx[j % KEY_SIZE], alphabet.index(el))
            j += 1 # переход к следующей букве ключевого слова
        else:
            # если символ - не буква, то добавляем его без изменений
            res += el

    # возвращаем зашифрованную строку
    return res

word = input().upper()

# тестирование
encoded_word_table = encode(word, way='table')
encoded_word_formula = encode(word)
assert encoded_word_table == encoded_word_formula, "методы дают разный результат"
res_dec = encode(encoded_word_formula, de=True)
assert word == res_dec, "неправильный алгоритм расшифровки"
# итоговый результат
print(word, "->", encoded_word_formula, sep="\n")
