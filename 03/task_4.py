"""
4. Написать программу, в которой реализовать две функции.

В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.

Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
Например:
[91, 42, 47, 64, 60, 23, 82, 78, 22, 15]
и
['zmsebjvdgi', 'ychpwljtzn', 'zqywoopbwf', 'nkxdnnqyhe', 'eqpbrjwjdp',
'sllbegvgmh', 'kzrmrozeco', 'jbppumpypu', 'jjsmronkvm', 'qtnspcleqd']


Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение.
Например:
91 zmsebjvdgi

42 ychpwljtzn

...

Первая функция должна возвращать ссылку на файловый дескриптор


После вызова первой функции возвращаемый файловый дескриптор нужно передавать во вторую функцию
Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
"""
import os.path

def example():
    while True:
        if os.path.isfile('filename.txt'):
            print ("Файл filename.txt уже существует")
            break
        try:
            print("Файл filename.txt не существует.\n"
                  "Для создания введите любое число.\n"
                  "Для выхода любую букву.")
            getNumber = int(input())
            if getNumber == int(getNumber):
                a = [91, 42, 47, 64, 60, 23, 82, 78, 22, 15]
                b = ['zmsebjvdgi', 'ychpwljtzn', 'zqywoopbwf', 'nkxdnnqyhe', 'eqpbrjwjdp',
                     'sllbegvgmh', 'kzrmrozeco', 'jbppumpypu', 'jjsmronkvm', 'qtnspcleqd']
                c = [a, b]
                with open("filename.txt", "w") as file:
                    for x in zip(*c):
                        file.write("{0}\t{1}\n".format(*x))
                print('Файл filename.txt был создан')
        except ValueError:
            print("Вы решили не создавать файл")
            break
        else:
            print()
            break
example()

