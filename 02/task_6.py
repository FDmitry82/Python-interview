"""
6. Проверить на практике возможности полиморфизма.

Необходимо разделить дочерний класс ItemDiscountReport на два класса.

Инициализировать классы необязательно.

Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены.

Далее реализовать выполнение каждой из функции тремя способами.
"""
class ItemDiscount:  # объявляем родительский класс
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

class ItemDiscountOneReport(ItemDiscount):  # объявляем 1 класс Инфо
    def get_info(self):
        print(self.get_name())

class ItemDiscountTwoReport(ItemDiscount):  # объявляем 2 класс Инфо
    def get_info(self):
        print(self.get_price())

ItemOne = ItemDiscountOneReport("Магнитафон", 100)
ItemOne.get_info()

ItemTwo = ItemDiscountTwoReport("Холодильник", 320)
ItemTwo.get_info()

for item in (ItemOne, ItemTwo):
    item.get_info()

def item_get(item):
    item.get_info()

item_get(ItemOne)
item_get(ItemTwo)