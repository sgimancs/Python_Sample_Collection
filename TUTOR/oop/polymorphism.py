# coding=utf-8
# **********************************
# ООП - П О Л И М О Р Ф И З М
# **********************************
# Writing sgiman, 2025

#==================================
# PERSON (base class)
#==================================
class Person:

    # CONSTRUCTOR (init)
    def __init__(self, name, age):
        self.__name = name      # устанавливаем имя
        self.__age = age        # устанавливаем возраст

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

    # METHOD
    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)


#==================================
# EMPLOYEE (extended class PERSON)
#==================================
class Employee(Person):
    # определение конструктора
    def __init__(self, name, age, company):
        Person.__init__(self, name, age)    # базовый класс
        self.company = company              # доп. свойство

    # переопределение метода display_info
    def display_info(self):
        Person.display_info(self)           # базовый класс
        print("Компания:", self.company)    # доп. функция (метод)


#==================================
# STUDENT (extended class PERSON)
#==================================
class Student(Person):
    # определение конструктора
    def __init__(self, name, age, university):
        Person.__init__(self, name, age)
        self.university = university            # доп. свойство

    # переопределение метода display_info
    def display_info(self):
        print("Студент", self.name, "учится в университете", self.university)


people = [Person("Tom", 23),
          Student("Bob", 19, "Harvard"),
          Employee("Sam", 35, "Google")]

for person in people:
    person.display_info()
    print()
