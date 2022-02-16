# Написать программу которая данный список кортежей переведет в список списков
# Входные данные: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
# Результат: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]
list_of_tuples: list = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
x, y, z, a = list_of_tuples
x: list = list(x)
y: list = list(y)
z: list = list(z)
a: list = list(a)
list_of_lists: list = [x, y, z, a]
print(list_of_lists)
