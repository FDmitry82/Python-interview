"""
Проверить механизм наследования в Python.

Для этого создать два класса. Первый — родительский (ItemDiscount),
должен содержать статическую информацию о товаре: название и цену.

Второй — дочерний (ItemDiscountReport),
должен содержать функцию (get_parent_data), отвечающую
за отображение информации о товаре в одной строке.

Проверить работу программы.
"""


class ItemDiscount:  # объявляем родительский класс
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ItemDiscountReport(ItemDiscount):  # объявляем класс наследник
    def get_parent_data(self):
        return f'Наименование товара: {self.name}, Стоимость: {self.price}'

Item = ItemDiscountReport("Магнитафон", 100)
print(Item.get_parent_data())