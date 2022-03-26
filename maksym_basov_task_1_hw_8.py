# Написать функцию которая будет принимать 3 аргумента (int) и находить максимум из них

def maximum(num1, num2, num3) -> int:
    max_list: int = max([num1, num2, num3])
    return max_list


print(maximum(1, 2, 3))
