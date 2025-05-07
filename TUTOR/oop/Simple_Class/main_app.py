# coding=utf-8
# **********************************
# ООП - SIMPLE CLASS
# **********************************
# Writing sgiman, 2025

from classes import Person, Auto    # import classes
# или можем подключить весь модуль
# import classes

print()
person1 = Person("Tom")
person1.display_info()

del person1  # удаление из памяти
# person1.display_info()  # Этот метод работать не будет, так как person1 уже удален из памяти

#--------------------------------------------------------------------------------------------------
print("-" * 80)

person2 = Person("Sam")
person2.display_info()

bmw = Auto("BMW")
bmw.move(65)
