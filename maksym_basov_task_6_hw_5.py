# Написать примеры всех методов из set объекта.
# Пример
# set1 = {1,2,3}
# # add
# set1.add(4)
# # update
# set1.update([2,3,4,5])
set1: set = {1, 2, 3}
set2: set = {1, 2, 3, 4, 5}
set1.clear()
set3: set = set1.copy
set1.intersection(set2)
set1.intersection_update(set2), set1 | set2
set1.issubset(set2)
set2.difference(set1)
set1.difference_update(set2)
set1.symmetric_difference(set2)
set1.symmetric_difference_update(set2)
set1.union(set2), set1 & set2
set1.issuperset(set2), set1 >= set2
set1.pop()
set1.remove(3)
