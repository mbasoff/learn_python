# Написать функцию которая будет принимать 2 аргумента (int) и находить максимум из них.
# Затем используя функцию1 (вызвать ее) написать функцию2 которая будет принимать 3 аргумента и находить максимум с помощью функции1.
# в итоге будет .
# псевдокод
# функция_нахождения_макс_из_2х(арг1, арг2):
# return максимальное значение из 2х аргументов
#
# функция_нахождения_макс_из_3х(арг1, арг2, арг3):
#  использую тут функция_нахождения_макс_из_2х()
# return максимальное значение из 3х аргументов.
global max_list


def maximum(num1, num2) -> int:
    max_list: int = max([num1, num2])
    return max_list


def maximum_wrapper(n1, n2, n3) -> int:
    max_list_: list = max([maximum(n1, n2), n3])
    return max_list_


print(maximum_wrapper(1, 2, 3))
