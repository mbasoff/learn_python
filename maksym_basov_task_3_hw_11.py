# написать функцию которая с помощью assert будет тестировать ваш самописный reduce
import maksym_basov_task_2_hw_11


def test_my_reduce():
    assert maksym_basov_task_2_hw_11.my_reduce(maksym_basov_task_2_hw_11.add, [1, 2, 3]) == 6


