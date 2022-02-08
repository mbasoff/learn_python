user_string: str = input("Введите строку ")
user_string_lowercase: str = user_string.lower()
user_string_lowercase_replaced: str = user_string_lowercase.replace('черт ', '####')
print(user_string_lowercase_replaced, sep=" ")
