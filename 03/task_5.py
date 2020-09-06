"""
5. Усовершенствовать первую функцию из предыдущего примера.

Необходимо просканировать текстовый файл, созданный на предыдущем задании
и реализовать создание и запись нового текстового файла

В новый текстовый файл обеспечить запись строк вида:

zmsebjvdgi zmsebjvdgi
ychpwljtzn ychpwljtzn
...

Т.е. извлекаются строки из первого текстового файла
а в новый они записываются в виде, где вместо числа ставится строка

Здесь необходимо использовать регулярные выражения.
"""

import os.path
import re
# from functools import reduce
import random

# STRING_SIZE = 10
# Функция генерирует строку из 10 случайных букв
# def random_string():
#     return reduce(lambda string, char: string + char,
#                   [chr(random.randint(ord('a'), ord('z'))) for _ in range(STRING_SIZE)])

def read2list():
    c = open("filename.txt", "r")
    d = open("filename_duble.txt", "w")

    for line in c:
        numb = re.search(r'\d*', line)
        string = re.search(r'\s\w*', line)
        line = line.replace(numb.group(0), string.group(0))
        d.write(line)

    c.close()
    d.close()

    with open("filename_duble.txt", encoding='utf-8') as descr:
        for elem in descr:
            print(elem)

read2list()