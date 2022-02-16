"""Программа принимает список продуктов и принтит самое длинное слово и его длинну.
Ипользовать ''.format() для вывода строки и аргументов.
Входные данные: ['bread', 'milk', 'kolbasa']
Результат: 'Самое длинное название продукта kolbasa длинна 7 символов'"""

my_list: list = ['bread', 'milk', 'kolbasa']
my_list_max: str = max(my_list, key=len)
my_list_max_length: int = len(my_list_max)

print("Самое длинное название продукта {} длинна {} символов".format(my_list_max, my_list_max_length))
