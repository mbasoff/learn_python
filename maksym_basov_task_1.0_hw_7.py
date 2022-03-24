# Для начала в одном файле.
# 1) 5 примеров list comprehension
# 2) 5 examples with DICT comprehension
# 3) 5 примеров с set comprehensions
# LIST comprehensions
squares: list = [x ** 2 for x in range(10)]
print(squares)
odds: list = [x for x in range(10) if x % 2 != 0]
print(odds)
seq: list = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(10)]
print(seq)
human_letters = [letter for letter in 'human']
print(human_letters)
matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)
# DICT comprehensions
dict1: dict = {key: value for key, value in zip([1, 2, 3], ['a', 'b', 'c'])}
print(dict1)
square_dict = {num: num * num for num in range(1, 11)}
print(square_dict)
dictionary = {k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)}
print(dictionary)
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_dict_1 = {k: ('old' if v > 40 else 'young')
              for (k, v) in original_dict.items()}
print(new_dict_1)
fruits = ['apple', 'mango', 'banana', 'cherry']
fruits_dict: dict = {f: len(f) for f in fruits}
print(fruits_dict)
# SET comprehension
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newSet = {element * 3 for element in myList}
print(newSet)
some_set: set = {x for x in range(2, 101)
                 if not any(x % y == 0 for y in range(2, x))}
print(some_set)
set1: set = {i for i in range(15)}
print(set1)
set2: set = {i for i in range(20) if i % 2 == 0}
print(set2)
