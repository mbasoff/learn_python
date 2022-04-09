# написать 3 примера генераторных функций с различными последовательностями.
# 1
def numbers_range(n):
    for i in range(n):
        yield i


a = numbers_range(4)

for b in a:
    print(b)

# 2

def subgenerator():
    yield 'Python'


def generator():
    yield 'I am'
    yield from subgenerator()
    yield 'developer'


for i in generator():
    print(i, end='\n')

# 3


def func_even(list_of_nums):
    for i in list_of_nums:
        if i % 2 == 0:
            yield i


list_of_nums = [1, 2, 3, 8, 15, 42]


print("Только четные числа: ", end=" ")
for i in func_even(list_of_nums):
    print(i, end=" ")