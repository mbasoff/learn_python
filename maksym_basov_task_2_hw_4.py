"""Написать программу, которая подсчитывает количество символов в строке
и формирует dict в котором key = буква, value= количество их в слове:
Входная строка : 'Hillel school'
Результат :  {'H': 1, 'i': 1, 'l': 3, 'e': 1, ' ': 1, 's': 1, 'c': 1, 'h': 1, 'o': 2}"""

check_string = "Hillel school"
my_dict = {}
for char in check_string:
    my_dict[char] = my_dict.get(char, 0) + 1
print(my_dict)
