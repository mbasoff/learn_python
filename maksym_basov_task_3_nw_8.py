#  с помощью Анонимной функции остортировать список кортежей по цифре.
# Пример(Example)
# Input: [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
# Otput: [('cola', 1), ('milk', 2), ('bread', 5), ('eggs', 30)]
input_list_of_tuples: list = [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
sorted_list_of_tuples: list = sorted(input_list_of_tuples, key=lambda j: j[1])
print(sorted_list_of_tuples)
