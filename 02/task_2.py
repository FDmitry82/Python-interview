"""
2. Инкапсулировать оба параметра (название и цену)
товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы
будет сгенерирована ошибка выполнения.
"""
class ItemDiscount:  # объявляем родительский класс
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

class ItemDiscountReport(ItemDiscount):  # объявляем класс наследник
    def get_parent_data(self):
        return f'Наименование товара: {self.name}, Стоимость: {self.price}'

Item = ItemDiscountReport("Магнитафон", 100)
print(Item.get_parent_data())
