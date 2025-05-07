# coding=utf-8
# Константа с именем файла
FILENAME = 'test.txt'

messages = list()   # список сообщений

# Выводим 4 запроса на ввод данных от пользователя
for i in range(4):
    message = input('Введите строку ' + str(i + 1) + ': ')
    messages.append(message + '\n')     # добавить в список сообщений

# Записываем введенные данные в файл (на добавление "a" c utf-8)
with open(FILENAME, 'a', encoding='utf-8') as file:
    for message in messages:
        file.write(message)             # записать строку

print('Читаем файл')
# Читаем все строки из файла (utf-8)
with open(FILENAME, 'r', encoding='utf-8') as file:
    for message in file:
        print(message, end='')
