# coding=utf-8
# **********************************
# ООП - Н А С Л Е Д О В А Н И Е
# **********************************
# Writing sgiman, 2025

#===================================
# PERSON (CLASS)
#===================================
class Person:

    # CONSTRUCTOR (init)
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age  # устанавливаем возраст

    # GETTER (decoration)
    @property
    def age(self):
        return self.__age

    # GETTER (decoration)
    @property
    def name(self):
        return self.__name

    # SETTER (decoration)
    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    # METHOD
    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)


#===================================
# EMPLOYEE (CLASS)
#===================================
class Employee(Person):
    def details(self, company):
        # print(self.__name, "работает в компании", company) # так нельзя, self.__name - приватный атрибут
        print(self.name, "работает в компании", company)


tom = Employee("Tom", 23)   # экземпляр (наследование от класса) - объект класса

tom.details("Google")
tom.age = 36
tom.display_info()
