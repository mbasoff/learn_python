# Написать функцию которая будет добовлять код страны
# к номеру телефона с помощью замыкания
# внешний вид вызова функции.
# my_number = user_telephone('+044')
# my_number('838372893')
# +044838372893 результат.

def user_telephone(part1) -> str:

    def user_telephone1(part2) -> str:
        return print(f'{part1}{part2}')

    return user_telephone1


my_number = user_telephone('+044')
my_number('838372893')
