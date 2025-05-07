# coding=utf-8
# **********************************
# ООП - О Б Ъ Е К Т (ЭКЗЕМПЛЯР)
# **********************************
# Writing sgiman, 2025

class Person:

    # CONSTRUCTOR (init)
    def __init__(self, name, age):
        self.__name = name          # устанавливаем имя
        self.__age = age            # устанавливаем возраст

    # GETTER (decoration)
    @property
    def name(self):
        return self.__name

    # GETTER (decoration)
    @property
    def age(self):
        return self.__age

    # SETTER (decoration)
    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    #----------------------------
    # METHOD (function)
    #----------------------------
    def display_info(self):
        print(self.__str__())

    # ДОПОЛНЕНИЕ МЕТОДА
    def __str__(self):
        return "Имя: {} \t Возраст: {}".format(self.__name, self.__age)


tom = Person("Tom", 23)     # Экземпляр
print(tom)
