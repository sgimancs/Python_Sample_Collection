import hashlib
import os

# Возвращает хэш-строку указанного имени файла.


def hashFile(filename):
    # Для больших файлов, если мы читаем их все вместе,
    # это может привести к переполнению памяти,
    # поэтому мы берем блок для чтения за раз.
    BLOCKSIZE = 65536
    hasher = hashlib.md5()

    with open(filename, 'rb') as file:
        # Считывает определенный размер блока из файла
        buf = file.read(BLOCKSIZE)
        while(len(buf) > 0):
            hasher.update(buf)
            buf = file.read(BLOCKSIZE)
    return hasher.hexdigest()


if __name__ == "__main__":
    # Словарь для хранения хеша и имени файла
    hashMap = {}

    # Список для хранения удаленных файлов
    deletedFiles = []
    filelist = [f for f in os.listdir() if os.path.isfile(f)]
    for f in filelist:
        key = hashFile(f)
        # Если ключ уже существует, файл удаляется.
        if key in hashMap.keys():
            deletedFiles.append(f)
            os.remove(f)
        else:
            hashMap[key] = f
    if len(deletedFiles) != 0:
        print('Deleted Files')
        for i in deletedFiles:
            print(i)
    else:
        print('No duplicate files found')
