# coding=utf-8
# **********************************
# ООП - SIMPLE CLASS (person)
# **********************************
# Writing sgiman, 2025

#===================================
# PERSON (CLASS)
#===================================
class Person:

    # конструктор
    def __init__(self, name):
        self.name = name

    # де-конструктор
    def __del__(self):
        print('__del__: ', self.name, " - deleted from memory")

    # метод (функция)
    def display_info(self):
        print('display_info: ', "Hi, my name is", self.name)


#===================================
# AUTO (CLASS)
#===================================
class Auto:

    # конструктор
    def __init__(self, name):
        self.name = name

    def move(self, speed):
        print(self.name, "едет со скоростью", speed, "км/ч")
