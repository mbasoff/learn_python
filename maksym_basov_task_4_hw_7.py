# Написать функцию которая принимает в качестве аргумента
# строку, и возвращает True, если строка является полиндромом и False если нет

def palindrome(input_string) -> bool:
    if str(input_string) == str(input_string)[::-1]:
        return True
    else:
        return False


print(palindrome('ma#am'))