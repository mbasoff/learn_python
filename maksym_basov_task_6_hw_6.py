# Посчитать общее количество наименований в списке. И только в списках.
# Example:
# shedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}
# Результат: 6

schedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}
my_list_of_lists: list = []
enum = []
count = 0

for val in schedule:
    my_list_of_lists += schedule.values()
    break


for item in my_list_of_lists:
    if isinstance(item, list):
        enum.append(item)
        continue


for element in enum:
    count += len(element)

print(count)