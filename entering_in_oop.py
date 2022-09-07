""" ООП - объектно-ориентированное программирование """
# Классы - участки кода, которые описывают какой-то тип данных/объект. 

# class MyClass:
    #  a = 10 # атрибут класса


# Атрибут класса - атрибут/переменная класса, которая относится ко всем созданным объектам/экземплярам от этого класса. У каждого объекта есть своя копия атрибутов.

# ********************************************************************************************************************

# class Human:
#     skin = True
#     hands = 2
#     head = 1


# h = Human() # объект/экземпляр класса
# print(type(h))
# print(h.hands)
# h.hands = 3
# print(h.hands)
# h2 = Human()
# print(h2.hands)

# ********************************************************************************************************************

# class Human:
#     hands = 2
#     head = 1
#     legs = 2
    
#     def __init__(self, age, height, weight):
#         self.age = age
#         self.height = height
#         self.weight = weight
#         # атрибуты экземпляра класса - атрибуты присущие конкретному объекту/экземпляру.

# human1 = Human(33, 186, 92)
# human2 = Human(height=164, age=23, weight=54)
# print(human1.legs, human1.hands, human1.head, human1.age, human1.height, human1.weight)
# print(human2.age)

# ********************************************************************************************************************

# Метод - функция, которая определена внутри класса и описывает какое-то действие.

# ********************************************************************************************************************

# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         #self  - ссылка на объект класса
#         print(f'{self.name} лает...')


# dog1 = Dog('Tuzik')
# dog1.bark()
# Dog.bark(dog1)

# ********************************************************************************************************************

# class Students:
#     course = 4

#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age

#     def get_info(self):
#         return f'{self.name} {self.last_name}, {self.age}'

#     def sleep(slef):
#         print('Спать во время занятий')

#     def write(self):
#         print('Пишу лекции')


# stud1 = Students('Vasya', 'Alekhin', 22)
# stud2 = Students('Imran', 'Bakaev', 21)
# stud3 = Students('Aygerim', 'Sydykova', 33)
# stud1.sleep()
# print(stud2.get_info())
# stud3.write()
# stud1.write()

# ********************************************************************************************************************

# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def birthday(self):
#         self.age += 1
#         return f'{self.name} исполнилось {self.age} лет! Поздравляем!!!'

# person1 = Person('Алекс', 23)
# print(person1.age)
# print(person1.birthday())
# print(person1.age)
# person1.legs = 3
# print(person1.legs)

# ********************************************************************************************************************

# class Cars:
#     car_counter = 0

#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#         Cars.car_counter += 1

#     def __str__(self):
#         return f'{self.color}, {self.model}'


# car1 = Cars('White', 'Toyota')
# print(car1.car_counter)
# car2 = Cars('Black', 'Honda')
# print(car2.car_counter)
# print(car1)

# ********************************************************************************************************************

# type(obj) - позволяет узнать тип объекта
# isinstance(obj, class) - возвращает True/False, если переданный объект принадлежит указанному классу.

# print(isinstance(12, int))

# int           |
# list          |
# dict          |
# tuple         | - Встроенные классы в Python.
# set           |
# bool          |
# frozenset     |

# ********************************************************************************************************************

""" 
Наследование    |
Инкапсуляция    | - Три основных принципа ООП
Полиморфизм     |


Агрегация       |
Абстракция      | - Три неосновных принципа ООП
Композиция      |
"""

# ********************************************************************************************************************

# class MyClass:
#     var1 = 10

#     def __init__(self):
#         self.var2 = 20
#         self.var3 = 30

# obj = MyClass()
# obj.var1 # 10
# obj.var2 # 20
# obj.var3 # 30
# obj.var4 = 40
# print(obj.__dict__)

# ********************************************************************************************************************

# setattr(obj, 'var5', 50) # obj.var5 = 50
# print(obj.var5) # 50
# print(hasattr(obj, 'var7')) # False
# print(getattr(obj, 'var1')) # obj.var1 - 10
# print(getattr(obj, 'var8', 'Нет такого атрибута')) # Нет такого атрибута

# ********************************************************************************************************************

# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('Объект создан!')
#         # __init__ - инициализатор объектов

#     def __del__(self):
#         print('Объект удален!')
#         # __del__ - финализатор объекта

# p1 = Person('Alexey', 33)
# p2 = Person('Alexandr', 35)
# p3 = Person('Anastasiya', 28)

# ********************************************************************************************************************

# class Product:
#     def __init__(self, title: str = 'Товар', price: float = 0.0, quantity: int = 0, desc: str = 'Нет описания'):
#         if not isinstance(title, str):
#             raise ValueError('title must be str')
#         self.title = title
#         self.price = price
#         self.quantity = quantity
#         self.desc = desc

# prod1 = Product(title=1234)
# print(prod1) # ValueError('title must be str')

# ********************************************************************************************************************

# from dataclasses import dataclass
# from typing import Any


# @dataclass
# class Product:
#     title: str
#     type_: Any
#     price: float = 0.0
#     quantity: int = 0
#     description: str = 'Нет описания'

# prod1 = Product(title=1234, type_='Rice', price=90.0, quantity=10)
# print(prod1.__dict__)

# ********************************************************************************************************************

# class Animals:
#     pass

# a = Animals()
# a.legs = 4
# print(a.__dict__)

# ********************************************************************************************************************

# class Cars:
#     __slots__ = ['model', 'color', 'brand']

#     def __init__(self, model, color, brand):
#         self.model = model
#         self.color = color
#         self.brand = brand

# car1 = Cars('Camry', 'White', 'Toyota')
# car1.volume = 3.5 # AttributeError
# print(car1.__dict__) # AttributeError
# print(dir(car1))

# ********************************************************************************************************************