""" Множественное наследование """

class Dad:
    eyes_color = 'green'
    hair_color = 'black'
class Mom:
    hair_color = 'brown'
    eyes_color = 'blue'

class Child(Dad, Mom):
    pass

child = Child()
# print(child.eyes_color)
# print(child.hair_color)

""" Поиск атрибутов и методов идет слева направо """

# ********************************************************************************************************************

# class.mro() - метод для получения списка порядка поиска методов и атрибутов - method resolution order

# print(Child.mro())

# ********************************************************************************************************************

""" Проблема ромба """

# class A:
#     def method(self):
#         print(A.__name__)

# class B(A):
#     def method(self):
#         print(B.__name__)

# class C(A):
#     def method(self):
#         print(C.__name__)

# class D():
#     def method(self):
#         # super().method() # обращение к родителю
#         A.method(self) # Делегирование
#         print('МЕТОД D')

# obj = D()
# obj.method()
# print(D.mro())

# ********************************************************************************************************************
""" Перекрестное наследование (не решено) """

# class A:
#     pass

# class B:
#     pass

# class C(A, B):
#     pass

# class D(B, A):
#     pass

# class E(C, D):
#     pass




# SOLID
# S - single responsibility
# O - open/closed
# L - Liskov substitution
# I - Interface segregation
# D - Dependency inversion

#                        """ S - single responsibility """

# class DateTemp:
#     def date(self):
#         print('Сегодня 9 сентября')

#     def temp(self):
#         print('Сейчас 40 градусов')

        
# class Date(DateTemp):
#     pass

# class Temp(DateTemp):
#     pass

# ********************************************************************************************************************

# class Date:
#     def date(self):
#         print('Сегодня 9 сентября')

# class Temp:
#     def temp(self):
#         print('Сейчас 30 градусов')


# class DateTemp(Date, Temp):
#     pass

# ********************************************************************************************************************