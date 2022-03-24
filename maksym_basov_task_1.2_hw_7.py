# написать функцию которая в качестве аргумента принимает размер стороны квадрата, а возвращает кортеж в котором лежат
# три значения:
#
# периметр квадрата
# диагональ квадрата
# площадь квадрата
import math


def square_calc(square_length) -> float:
    sq_per = 4*square_length
    sq_diag = math.sqrt(2*square_length**2)
    sq_area = square_length**2
    result: list = [sq_per, sq_diag, sq_area]
    return tuple(result)


print(square_calc(3))