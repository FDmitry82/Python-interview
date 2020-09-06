"""
3. Усовершенствовать родительский класс таким образом,
чтобы получить доступ к защищенным переменным.
"""
class ItemDiscount:  # объявляем родительский класс
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

class ItemDiscountReport(ItemDiscount):  # объявляем класс наследник
    def get_parent_data(self):
        return f'Наименование товара: {self.get_name()}, Стоимость: {self.get_price()}'

Item = ItemDiscountReport("Магнитафон", 100)
print(Item.get_parent_data())