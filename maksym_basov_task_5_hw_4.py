"""Тема приведение типов. Работа со списком. Расчленение строки и ее соединение.
Пользователь вводит через запятую последовательность слов например цвета или продукты.
Программа возвращает уникальные слова отсортированные по алфавиту.
Входные данные: red, white, black, red, green, black
Результат: black, green, red, white"""

input_string: str = input('Введите строку \n')
input_string_replaced: str = input_string.replace(' ', '')
input_string_split: str = input_string_replaced.split(',')
input_string_set: set = set(input_string_split)
input_string_list: list = list(input_string_set)
input_string_list_sorted: list = sorted(input_string_list)
input_string_list_sorted_join: str = ", ".join(input_string_list_sorted)
print(input_string_list_sorted_join)
