# Вернуть из dictionary все уникальные values.
# Пример
# Входные данные = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Результат = {'S001', 'S005', 'S007', 'S002', 'S009'}
# Усложнение! +5 points
# Вернуть ту же структуру.
# После dictionary L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S005"}, {"V":"S009"},{"VIII":"S007"}]

input_data: list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
my_list: list = []

for val in input_data:
    my_list += val.values()

my_set: set = set(my_list)
print(my_set)





