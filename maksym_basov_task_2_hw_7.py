# написать функцию которая принимает в качестве аргумента номер месяца, в возвращает строку - время года, этого месяца

def season(number_of_month) -> str:
    if number_of_month in range(1, 3):
        return 'Winter'
    elif number_of_month in range(3, 6):
        return 'Spring'
    elif number_of_month in range(6, 9):
        return 'Summer'
    elif number_of_month in range(9, 12):
        return 'Autumn'
    elif number_of_month == 12:
        return 'Winter'
    else:
        return 'Please enter number of month in range from 1 to 12'


print(season(13))
