# написать программу которая будет создавать список методов из доступных методов питон объектов. Под доступными подразумевается
# методы без подчеркиваний. Фунции dir()
# т.е для объекта set должен быть список методов
#
# ['add',
#  'clear',
#  'copy',
#  'difference',
#  'discard',
#  'intersection',
#  'isdisjoint',
#  'issubset',
#  'issuperset',
#  'pop',
#  'remove',
#  'union',
#  'update']
import re

dir_list: list = dir(set)
filtered_list: list = [x for x in dir_list if '__' not in x]
print(filtered_list, sep="\n")
