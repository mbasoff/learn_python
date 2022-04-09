# написать функцию которая принимает от пользователя 2 аргумента и делит онин на другой.
# при попытке деления на ноль вывести пользователю "ай яй яй делить на ноль можно не многим"
# Все остальные исключения с поймать и вывести их значение в текстовом формате.
# И в любом случае вывести. " I 'am happy that you learn python"


d1 = input('Enter first argument\n')
d2 = input('Enter second argument\n')


def my_division(d1: int, d2: int) -> float:
    try:
        return float(d1) / float(d2)
    except ZeroDivisionError:
        print('ай яй яй делить на ноль можно не многим')
    except Exception as error:
        print(error)
    finally:
        print("I 'am happy that you learn python")


print(my_division(d_1, d_2))
