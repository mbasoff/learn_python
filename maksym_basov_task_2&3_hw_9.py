# 2. Написать функцию которая будет у пользователя брать python обект в любом
# виде и выводить все его не магические методы в списке.
# и написать декторатор который будет выводить колличество методов в объекте.
#
# Похожую задачу мы уже решали. Можете взять решение из предыдущей . Но декоратор уже ваш полностью)
#
# func(tuple())
# [count, index]
#
# @methods_amount
# [count, index]
# 2
# 3.дописать декоратор, чтобы он принимал аргумент, например текст.
# и выводил его тоже.
#
# @methods_amount('need to learn')
# [count, index]
# 'need to learn 2'
import re


def methods_amount(text: str) -> str:
    def methods_amount_decorator(func) -> int:
        def wrapper(*args, **kwargs):
            counted_amount: list = func(*args, **kwargs)
            list_len: int = len(counted_amount)
            return print(f'{text} {list_len}')
        return wrapper
    return methods_amount_decorator


@methods_amount('Need to learn')
def filtered_methods(py_obj) -> list:
    dir_list: list = dir(py_obj)
    filtered_list = [x for x in dir_list if '__' not in x]
    return filtered_list


filtered_methods(set)
