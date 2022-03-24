# отсортировать словарь по ключам
my_dict: dict = {'a': 15, 'c': 110, 'b': 4, 'd': 77}

sorted_tuple = sorted(my_dict.items())
my_dict_sorted: dict = dict(sorted_tuple)

print(my_dict_sorted)
