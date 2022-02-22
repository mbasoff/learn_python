# Дан список с повторяющимися значениями необходимо из него удалить все определенные значения используя while цикл.
# Входные данные: ['bear', 'milk', 'eg', 'eg', 'eg', 'eg'] удалить все eg
# Результат: ['bear', 'milk']
some_list: list = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']

while 'eg' in some_list:
    some_list.remove('eg')
    continue
else:
    print(some_list)
