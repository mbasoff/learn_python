print("Hi py dev")
nickname: str = input("Enter nickname ")
age: int = input("Enter your age ")
gender: str = input("Enter your gender ")
age = int(age)
nickname = str(nickname)
if 'admin' in nickname:
    print('Привет', 'повелитель', sep=', ', end='!')
    input('')
elif (age < 11) and 'М' in gender:
    print('''Советую Вам посмотреть "TMNT"''')
elif (10 > age <= 14) and ('М' in gender) or (age > 30 and 'М' in gender):
    print("""Советую Вам посмотреть "StarWars" или 'Мандалорец'""")
elif 22 >= age <= 32 and 'Ж' in gender:
    print("""Советую Вам посмотреть "Трансформеры""""")
elif 16 < age and 'Ж' in gender:
    print("""Советую Вам посмотреть "Инсургент""""")
elif 'Женя' in nickname:
    print("Советую Вам посмотреть 'TENET'")
if 'Guido' in nickname:
    print('Огромное', 'спасибо')

