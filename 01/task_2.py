"""
Задание 2.	Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):

    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    заполните далее

Пример:
[
('mainapp', 'admin.py'),
('mainapp\\management\\commands', 'seed_db.py'),
...
]
"""
import inspect, os

def print_directory_contents():
    print('\nПуть каталога где вы сейчас находитесь\n',
          os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
    print('\nСписок всех файлов каталога где вы сейчас находитесь\n',
          os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
    for name in os.listdir():
        print(name)
    return

print_directory_contents()