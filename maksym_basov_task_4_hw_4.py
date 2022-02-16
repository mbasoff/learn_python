"""Пользователь водит свое имя.
Возвращается тектс в БОЛЬШОМ и маленьком регистре. Использовать ' '.format().
Для вставки аргументов в текст.
Входные данные: Apollo
Результат: APPOLLO apollo"""

user_name: str = input('Enter your name, please\n')
user_name_lower = user_name.lower()
user_name_upper = user_name.upper()

print('{user_name_upper} {user_name_lower}'.format(user_name_lower=user_name_lower, user_name_upper=user_name_upper))
