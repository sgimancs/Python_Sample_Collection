# Импортируем модуль для работы с бинарными файлами (standard)
import pickle

# Константа с именем файла
FILENAME = 'test.dat'

#-------------------------------------------------------
# ЗАПИСЬ-ЧТЕНИЕ ДЛЯ ОДНОЙ ЗАПИСИ
#-------------------------------------------------------
name = 'User'
age = 1

# Записываем несколько строк в файл
with open(FILENAME, 'wb') as file:
    # С помощью dump происходит последовательная запись объектов
    pickle.dump(name, file)
    pickle.dump(age, file)

# Читаем данные из файла
with open(FILENAME, 'rb') as file:
    # Поэтому при чтении используем load, для последовательного чтения объектов
    name = pickle.load(file)
    age = pickle.load(file)
    print('\nName:', name, '\nAge:', age)

#-------------------------------------------------------
# ЗАПИСЬ-ЧТЕНИЕ ДЛЯ СПИСКА (continue)
#-------------------------------------------------------
# Версия с записью и чтением набора объектов (список с вложенными подсписками)
users = [
    ["User1", 1, True],
    ["User2", 2, False],
    ["User3", 3, False]
]

# Записываем объект в файл
with open(FILENAME, "wb") as file:
    pickle.dump(users, file)

# Читаем объект из файла
with open(FILENAME, "rb") as file:
    users_from_file = pickle.load(file)
    for user in users_from_file:
        print("\nName:", user[0], "\nAge:", user[1], "\nPython developer:", user[2])
