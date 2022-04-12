# Сделать примеры в файлике.
# __call__
# __repr__
# @classmethod &@staticmethod
# @property, setter, deleter

# __call__
class MyClass:
    def __init__(self):
        print("MyClass created")

    def __call__(self):
        print("MyClass is called via special method")


x = MyClass()
# __repr__


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        repres = 'Person(' + self.name + ',' + str(self.age) + ')'
        return repres


person = Person("John", 20)
print(repr(person))

# @classmethod &@staticmethod


from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('Maks', 33)
person2 = Person.fromBirthYear('Maks', 1989)

print(person1.age)
print(person2.age)

print(Person.isAdult(33))

# @property, setter, deleter


class Car:

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("Please enter a valid price")

    @price.deleter
    def price(self):
        del self._price