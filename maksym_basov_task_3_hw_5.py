# Тема while and else
# дан список произвольный с int нужно вывести "all numbers are even" если все четные и NO если нет
#
# Пример входных данных: [11, 23, 65, 44, 76, 533]
# Результат: NO
#
# Пример входных данных: [12, 22, 66, 44, 76, 534]
# Результат: all numbers are even
import nums_from_string

even_or_odd: str = input("Enter list of numbers\n")
even_or_odd_nums: list = nums_from_string.get_nums(even_or_odd)
index: int = 0

while True:

    for index, value in enumerate(even_or_odd_nums):
        if 0 != (value % 2):
            print('NO')
            break

        else:
            index += 1
            continue

    else:
        print('all numbers are even')
    break
