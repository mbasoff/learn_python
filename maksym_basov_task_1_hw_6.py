# сложить словари в один.
# использовать for и dict methods.
from typing import Dict

first: dict[int, int] = {1: 10, 2: 20}
second: dict[int, int] = {3: 30, 4: 40}
third: dict[int, int] = {5: 50, 6: 60}
fourth: dict[int, int] = {7: 70, 8: 80}
fifth: dict[int, int] = {9: 90, 10: 100}

combined_dict: dict = {**first, **second, **third, **fourth, **fifth}

print(combined_dict)


