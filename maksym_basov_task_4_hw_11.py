#  Создать класс с методом которого можно будет возвращать область видимости созданного экземпляра класса.
# В конструкторе(__init__) вашего класса пускай будут те параметры которые вы захотите.
from pprint import pprint


class MySpace:
    a = 'abra'

    def __init__(self):
        print(self.a + 'cadabra')

    def return_(self):
        pprint(globals())


t = MySpace()
t.return_()
