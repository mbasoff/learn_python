# В другом файлике
# сделать пример функции
# без return c pass or ...
# сделать 5 различных функций на свое усмотрение.

def func1(a) -> str:
    pass


def func2(b) -> int:
    ...


def multiplication(m1, m2) -> int:
    return m1 * m2


print(multiplication(2, 7))


def division(d1, d2) -> float:
    try:
        x: float = float(d1 / d2)
        return x
    except ZeroDivisionError:
        print('Please do not divide by zero')


print(division(1, 0))


def sum_of_numbers(s1, s2) -> int:
    return s1 + s2


print(sum_of_numbers(1, 2))


def subtraction(sub1, sub2) -> float:
    sub: float = sub1 - sub2
    return sub


print(subtraction(1, 2))


def percent_calc(value, perc_value) -> float:
    perc: float = (value/100) * perc_value
    return f'{perc} is {perc_value} % from {value}'


print(percent_calc(102, 20))