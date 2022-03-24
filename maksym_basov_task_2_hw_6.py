# 1. Создать словарь с ключами от 11 до 20 включительно. Значения = квадраты ключей
# Пример:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15:
# 225}
# 2. просуммировать все значения(values), делается в одну строку.(look build in functions)

my_dict: dict = {key: key ** 2 for key in range(11, 21)}
print(my_dict)

sum_of_values: int = sum(my_dict.values())
print(sum_of_values)




