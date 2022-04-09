# Попробовать посмотреть на написанный код и сделать его более надежным. Любые изменения приветствуются.
# просмотреть каждую программу и посмотреть как она может упасть. Попробовать ее зафейлить.
# Во время тестирования заметить какие ошибки появляется
# используя исключения изменить код. И не только исключения, а и фантазию.


# def example1():
#     try:
#         for i in range(3):
#             x = int(input("enter a number: "))
#             y = int(input("enter another number: "))
#             print(x, '/', y, '=', x / y)
#     except ZeroDivisionError:
#         print('Division by zero is not allowed')
#     except Exception as err:
#         print(err)
#
#
# def example2(L):
#     print("\n\nExample 2")
#     sum = 0
#     sumOfPairs = []
#     try:
#         for i in range(len(L)):
#             sumOfPairs.append(L[i + 1])
#             sum += 1
#         print("sumOfPairs = ", sumOfPairs)
#     except IndexError:
#         print('There is no element with this index')
#     except TypeError:
#         print('Enter the same type of data please')


def printUpperFile(fileName):
    with open(fileName, 'a+') as file:
        file.write('ndfhdjhfudj')
        for line in file:
            print(line.upper())



def main():
    # example1()
    # L = [10, 3, 5, 6, 9, 3]
    # example2(L)
    # example2([10, 3, 5, 6, "NA", 3])
    # example2([10, 3, 5, 6])

    printUpperFile("doesNotExistYest.txt")
    printUpperFile("misspelled.txt")


main()
