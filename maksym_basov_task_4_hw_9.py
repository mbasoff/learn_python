# Ваша задача - создать декоратор для функции, которая принимает неограниченное
# количество позиционных ХЕШИРУЕМЫХ элементов.
#
# Декоратор добавляет следующий функционал:
# Если функция уже вызвалась с такими аргументами - ваша функция должна
# вернуть результат выполнения этой функции из памяти, а не вычислять его заного.
# Если не вызывалась - вычислить результат, положить его в память, и вернуть.
#
# Подсказка - тут вам пригодятся словари.


hashable_dict = dict()


# def hashable_decorator(*args) -> dict:
#     def wrapper_hashable(func):
#         keys_list: list = hashable_dict.keys()
#         for i in keys_list:
#             if args not in keys_list:
#                 func(*args)
#             else:
#                 for j in keys_list:
#                     if j in keys_list:
#                         print(j)
#         return wrapper_hashable
#     return hashable_decorator


#@hashable_decorator
def hashable_(*args) -> dict:
    try:
        for i in args:
            hashable_dict: dict = {key: hash(args) for key in args}
            return hashable_dict
    except TypeError:
        print('Argument is not hashable')


x = hashable_(2,'heuhf')

print(x)
