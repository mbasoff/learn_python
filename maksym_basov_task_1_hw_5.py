# пользователь вводит пароль первый раз система запоминает и просит повторить пароль проверяет
# его если нет то просит повторить. А если совпал то сообщение.
import hashlib

user_password: str = input('Введите пароль\n')
user_password_hash: hash = hashlib.sha256(user_password.encode())
user_password_repeat: str = input('Введите пароль еще раз\n')
user_password_repeat_hash: hash = hashlib.sha256(user_password_repeat_hash.encode())


while user_password_hash == user_password_repeat_hash:
    print('Пароль верен')
    break
else:
    print('Введите пароль еще раз')
