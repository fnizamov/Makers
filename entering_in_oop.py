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

class Cars:
    car_counter = 0

    def __init__(self, color, model):
        self.color = color
        self.model = model
        Cars.car_counter += 1

    def __str__(self):
        return f'{self.color}, {self.model}'


car1 = Cars('White', 'Toyota')
# print(car1.car_counter)
car2 = Cars('Black', 'Honda')
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