"""
1. Написать программу, которая будет содержать функцию
для получения имени файла из полного пути до него.

При вызове функции в качестве аргумента должен передаваться путь до файла.
В функции необходимо реализовать «выделение» из этого пути имени файла (без расширения).

Пример:
функция принмает следующую строку - '../mainapp/views.py'

Результат:
views
"""
from os import path

def filepath(file):
    full_name = path.basename(file)
    name = path.splitext(full_name)[0]
    return print(name)

file = ('../mainapp/views.py')
filepath(file)
