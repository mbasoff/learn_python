# написать свою реализацию функции reduce() с описание в инлайновых и многострочных комментариях
# ее работы.
# def my_reduce(): моя реализация. (постарайтесь по памяти реализовать.)


def my_reduce(function, iterable, initializer=None):
    it = iter(iterable) # создание объекта итерируемого объекта
    if initializer is None: # проверка инициализатора, по умолчанию его нет
        value = next(it) # присваивание переменной значения элемента итерируемого объекта
    else:
        value = initializer # если есть параметр инициализации, то он
        # присваивается значению элемента итерируемого объекта
    for element in it: # для каждого значения в итерируемом объекте применяется фунция-аргумент
        value = function(value, element)
    return value


def add(a1, a2):
    return a1+a2

