#создаем базу интересующего треда
#метод шерудит по треду сверяясь с базой
#если в базе нет чего - добавляем
#теперь скачиваем этот свежак
import requests
import sqlite3 as sl
import api2ch

#проверка адреса
def address_checker(address: str):
    print(address)

#проверка треда на задвоение
def thread_doube_checker(address: str):
    pass

#создание новой папки для скачивания
def folder_maker(address: str):
    pass

#создание таблицы в базе данных
def db_table_maker(address: str):
    pass

#считка, выводит содержимое базы
def get_data(self, thread):
    with con:
        data = con.execute("SELECT * FROM thread")
        for row in data:
            print(row)

#downloading
def download(content_dict):
    for key, value in content_dict.items():
        print('Downloading file', key, 'from', value)
        url = value
        r = requests.get(url, allow_redirects=True)
        open('C:/files/2ch_scraper/content/' + str(key), 'wb').write(r.content)


#вставка, принимает имя треда str и словарь с добавляемой парой
def set_data(self, thread, insert_dict):
    data = []
    for key, value in insert_dict.items():
        sql = 'INSERT INTO ' + thread + ' (filename, link) values(?, ?)'
        item = (key, value)
        data.append(item)
    with con:
        con.executemany(sql, data)


#загоняем данные в базу
def set_data(thread, content_dict):
    pass

#читаем базу (проверка)
def get_data(thread):
    pass


URL = 'https://2ch.hk/b/res/259496296.html'



api = api2ch.DvachApi('b')

#получить номер треда из командной строки
thread = 259496296

#работа апишки
thread = api.get_thread(thread)

#создаем папку в папке content под контент

#создаем или подключаемся к существующей базе
con = sl.connect(thread)

#Создаем таблицу нового треда
with con:
    con.execute("""
        CREATE TABLE """ + thread + """ (
            filename TEXT UNIQUE NOT NULL PRIMARY KEY
            link TEXT
        );
    """)

content_dict = {}




#Файлы в треде
for post in thread:
    for file in post.files:
        #print(file.fullname, f'({file.name})', api2ch.CHAN_URL + file.path)
        #print(f'{file.name}', api2ch.CHAN_URL + file.path)
        #content_list.append(str(api2ch.CHAN_URL + file.path))
        content_dict[file.name] = api2ch.CHAN_URL + file.path

if __name__ == '__main__':
    address = 'https://2ch.hk/b/res/259496296.html'
    address_checker(address)

