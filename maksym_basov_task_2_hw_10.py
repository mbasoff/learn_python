# Скинуть файлик с примерами всех конструкций КРОМЕ менеджера контекста. With/as

# Конструкция try/except
my_list = [1, 2, 3, 4, 5]

try:
    my_list[6]
except IndexError:
    print("That index is not in the list!")

# Конструкция try/except/else

my_dict = {"a": 1, "b": 2, "c": 3}

try:
    value = my_dict["a"]
except KeyError:
    print("A KeyError occurred!")
else:
    print("No error occurred!")

# Конструкция try/except/finally

my_dict = {"a": 1, "b": 2, "c": 3}

try:
    value = my_dict["d"]
except KeyError:
    print("A KeyError occurred!")
finally:
    print("The finally statement has executed!")
