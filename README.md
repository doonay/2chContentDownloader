# 2chContentDownloader

Что требуется допилить:<br>
- вывод слова Done! сделать своевременным
- цвет шрифта в текстинпуте сделать более отчётливым на моменте вывода названия борды
- создание директории с названием борды и поддиректории с номером треда
- Какой-нибудь прогрессбар
- SQL учёт уже скачанного контента

![image](https://user-images.githubusercontent.com/18138614/175891891-90cd901a-94c7-46ec-bf52-954dd73bf1da.png)


bytes_converter - конвертирует размер в мегабайты<br>
filemanager - создает папки, файлы, работает с именами<br>
parser - парсит название треда, количество файлов, ссылки на файлы, размеры (общий и каждого отдельно)<br>
rus_gramary - изменяет окончание в зависимости от количества<br>
simple_async_downloader - простой асинхронный даунлоадер<br>
httplib2_downloader - простой синхронный даунлоадер (всё равно узкое место - запись на диск)<br>
SQL - для ведения учёта уже скачанного контента<br>
START - точка входа с ГУИ<br>
validator - проверяет введенный адрес треда на валидность<br>
style.qss - стиль ГУИ<br>

