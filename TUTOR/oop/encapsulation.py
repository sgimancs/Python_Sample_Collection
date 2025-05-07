# coding=utf-8
# **********************************
# ООП - И Н К А П С У Л Я Ц И Я
# **********************************
# Writing sgiman, 2025

# __var - private
# _var,var - public

class Person:

    # CONSTRUCTOR (init)
    def __init__(self, name):
        self.__name = name      # устанавливаем имя
        self.__age = 1          # устанавливаем возраст

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


    #----------------------------
    # METHOD (function)
    #----------------------------
    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)

tom = Person("Tom")     # Экземпляр

tom.display_info()      # Имя: Tom  Возраст: 1
tom.age = -3486         # Недопустимый возраст
print(tom.age)          # 1
tom.age = 36
tom.display_info()      # Имя: Tom  Возраст: 36

