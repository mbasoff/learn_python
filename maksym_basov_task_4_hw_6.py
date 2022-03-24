# Удалить дубликаты из dictionary
# пример
# Before :
#
# {'id1':
# {
# 'name': 'Ruslan',
# 'class': 1,
# 'subjects' : {'Math', 'Algorithms', 'English'}
# },
# 'id2':
# {
# 'name': 'Mark',
# 'class': 2,
# 'subjects' : {'Geometry', 'Java', 'Cooking'}
# },
# 'id3':
# {
# 'name': 'Ruslan',
# 'class': 1,
# 'subjects' : {'Math', 'Algorithms', 'English'}
# }
# }
#
# After:
# {'id1':
# {
# 'name': 'Ruslan',
# 'class': 1,
# 'subjects' : {'Math', 'Algorithms', 'English'}
# },
# 'id2':
# {
# 'name': 'Mark',
# 'class': 2,
# 'subjects' : {'Geometry', 'Java', 'Cooking'}
# }
my_dict: dict = {'id1':
    {
        'name': 'Ruslan',
        'class': 1,
        'subjects': {'Math', 'Algorithms', 'English'}
    },
    'id2':
        {
            'name': 'Mark',
            'class': 2,
            'subjects': {'Geometry', 'Java', 'Cooking'}
        },
    'id3':
        {
            'name': 'Ruslan',
            'class': 1,
            'subjects': {'Math', 'Algorithms', 'English'}
        }
}

for student in my_dict:
    if my_dict['id1']['name'] == my_dict['id2']['name'] or my_dict['id2']['name'] == my_dict['id3']['name'] or my_dict['id1']['name'] == my_dict['id3']['name']:
        del my_dict['id3']
        break
    else:
        print('There is no matches')

print(my_dict)