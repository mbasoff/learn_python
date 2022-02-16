# Тема Кортеж и работа сним.
# Удалить элемент из кортежа.
# Входные данные: (1, 2, 3)
# Результат: (1, 2)
some_tuple: tuple = (1, 2, 3)
some_list: list = list(some_tuple)
deleted_value: int = some_list.pop()
tuple_del: tuple = tuple(some_list)
print(tuple_del)
