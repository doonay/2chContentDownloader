from PyQt5.QtWidgets import *
from validator import Validator
from bytes_converter import BytesConverter
from rus_gramary import rus_gramary
import simple_async_downloader

from parser import Parser
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import asyncio
from PyQt5.QtCore import QThread
from PyQt5 import QtCore
import os
from PyQt5 import QtCore, QtWidgets, QtSql, QtGui
from PyQt5.Qt import *

import sys

def get_window_center(desktop_coordinate, window_coordinate):
    pos_coordinate = (desktop_coordinate // 2) - (window_coordinate // 2) #ширина стола разделить на два - (ширина окна разделить на два) (лево-право)
    return pos_coordinate



################################### ПАРАЛЛЕЛЬНЫЕ ПОТОКИ ###################################
class FileCountParserThread(QThread):
    finish_signal = pyqtSignal(dict) # ожидаемый тип возвращаемых данных dict

    def __init__(self, parent=None):
        super(FileCountParserThread, self).__init__(parent)

    thread_link = '' #<--- входные данные, которые мы получаем для расчётов
    #print('в потоке счётчика')
    
    def run(self):
        parser = Parser()
        #screen.btn_download.setEnabled(True)
        info = asyncio.run(parser.get_file_count(self.thread_link))
        #print(info)
        #round_size_string = str(round(info.get('total size')/1024, 1))
        self.finish_signal.emit(info) #<--- возвращаемые данные, которые мы получили в результате расчётов

        #progressbar_start_text = 'Всего ' + str(info.get('files')) + ' файла, общим объёмом ' + round_size_string + 'Mb'
        #print(progressbar_start_text)
        #https://2ch.hk/wp/res/69966.html
        #filelist = asyncio.run(parser.get_file_list(self.thread_link))
        #data = [info.get('files'), round_size_string, filelist] #int, str, list of dict
        #return(data)
        #print('FileCountParserThread.run done')
        #print(dir(self))
        #print(data)


class BoardNameParserThread(QThread):
    finish_signal = pyqtSignal(str) # ожидаемый тип возвращаемых данных str

    def __init__(self, parent=None):
        super(BoardNameParserThread, self).__init__(parent)

    #board_name = '' #<--- входные данные, которые мы получаем для расчётов
    thread_url = '' #<--- входные данные, которые мы получаем для расчётов
    #print('в потоке имени')

    def run(self):
        parser = Parser()
        board_name = asyncio.run(parser.get_board_name(self.thread_link))
        #board_name = asyncio.run(parser.get_board_name(self.thread_url))
        #print(board_name)
        self.finish_signal.emit(board_name) #<--- возвращаемые данные, которые мы получили в результате расчётов

class ContentListParserThread(QThread):
    finish_signal = pyqtSignal(list) # ожидаемый тип возвращаемых данных dict

    def __init__(self, parent=None):
        super(ContentListParserThread, self).__init__(parent)

    thread_link = '' #<--- входные данные, которые мы получаем для расчётов
    #print('в потоке парсера')
    
    def run(self):
        parser = Parser()
        #screen.btn_download.setEnabled(True)
        content_list = asyncio.run(parser.get_content_list(self.thread_link))
        #print(content_list)
        #round_size_string = str(round(info.get('total size')/1024, 1))
        #print(content_list)
        
        self.finish_signal.emit(content_list) #<--- возвращаемые данные, которые мы получили в результате расчётов

class DownloaderThread(QThread):
    finish_signal = pyqtSignal(str) # ожидаемый тип возвращаемых данных str

    def __init__(self, parent=None):
        super(DownloaderThread, self).__init__(parent)

    content_list = '' #<--- входные данные, которые мы получаем для расчётов

    #print(content_list, 'в потоке даунлоадера')

    def run(self):
        #asyncio.run(simple_async_downloader.list_downloader(self.content_list))
        #print(tupe(content_list), 'это в потоке довнлоадера')
        simple_async_downloader.list_downloader(self.content_list)
        self.finish_signal.emit('Done!') #<--- возвращаемые данные, которые мы получили в результате расчётов

    

##########################################################################################

class QMainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.thread_link = None
        self.info = None
        self.board_name = None
        self.content_list = None

        self.setWindowTitle('2ch Content Downloader')
        QFontDatabase.addApplicationFont("assets/fonts/AdventPro-Bold.ttf")

        content_count = 0

        ### ЛЭЙБЛ ###
        self.title = QLabel('2chDownloader')
        self.title.setAlignment(Qt.AlignLeft)
        self.title.setFont(QFont('Advent Pro SemiBold', 25))

        ### ПОЛЕ ДЛЯ ВВОДА ССЫЛКИ ###
        self.input_thread = QLineEdit()
        self.input_thread.setPlaceholderText('Link to thread...')
        self.input_thread.setFont(QFont('Advent Pro', 26))
        self.input_thread.textChanged.connect(self.link_validator) # Проверяем на валидность ссылку на тред

        ### КНОПКА Download ###
        self.btn_download = QPushButton('Download')
        self.btn_download.setFont(QFont('Advent Pro', 12))
        self.btn_download.clicked.connect(self.button_pressed)
        self.btn_download.setEnabled(False)

        '''
        ### ПРОГРЕССБАР ###
        self.progress = QProgressBar()
        self.progress.setAlignment(Qt.AlignCenter)
        self.progress.setFont(QFont('Advent Pro', 12))
        '''
        ### ЛЭЙБЛ ###
        self.processbar = QLabel('')
        self.processbar.setAlignment(Qt.AlignCenter)
        self.processbar.setFont(QFont('Advent Pro', 12))

        ### КОРОБКА ГОРИЗОНТАЛЬНАЯ ###
        hbox = QHBoxLayout()
        hbox.setSpacing(10)
        hbox.addWidget(self.input_thread)
        hbox.addWidget(self.btn_download)
        
        ### КОРОБКА ВЕРТИКАЛЬНАЯ ###
        vbox = QVBoxLayout()
        vbox.setSpacing(10)
        vbox.addWidget(self.title)
        vbox.addLayout(hbox)
        #vbox.addWidget(self.progress)
        vbox.addWidget(self.processbar)

        self.setLayout(vbox)

        #self.fileCountParserThread = FileCountParserThread(self)                       #можно создать поток прям при инициализации гуя, если данные уже есть
        #self.fileCountParserThread.finish_signal.connect(self.stop_gif)                #и сразу запустить его


        

    def link_validator(self):
        '''
        Тут проверяем текст введенный в поле на валидность
        print(self.input_thread.text(), 'должен быть ссылкой типа https://2ch.hk/wp/res/69966.html
        и в случае валидации передаем ссылку в метод подсчёта файлов
        '''
        validator = Validator()
        if validator.validator(self.input_thread.text()):
            print('парсер стартанул')
            self.logic()
        else:
            print('парсер не стартует')

    def logic(self):
        self.thread_link = self.input_thread.text()
        #self.input_thread.setEnabled(False)
        #Парсим количество файлов в треде в отдельном потоке
        self.FileCountParserThread_instance = FileCountParserThread() # создаем поток парсинга количества контента
        self.FileCountParserThread_instance.finish_signal.connect(self.process_bar_change) # это финишный сигнал для возврата
        self.FileCountParserThread_instance.thread_link = self.input_thread.text() # Передаем текст из поля для ввода (ссылку) в переменную потока
        self.FileCountParserThread_instance.start() # Стартует метод потока run

        #Парсим имя доски
        self.BoardNameParserThread_instance = BoardNameParserThread() # создаем поток получения имени
        self.BoardNameParserThread_instance.finish_signal.connect(self.inputtext_to_board_name) # это финишный сигнал для возврата
        self.BoardNameParserThread_instance.thread_link = self.input_thread.text() # Передаем текст из поля для ввода (ссылку) в переменную потока
        self.BoardNameParserThread_instance.start() # Стартует метод потока run
           
        #self.input_thread.setText(self.board_name)
        #self.btn_download.setEnabled(True)

        self.ContentListParserThread_instance = ContentListParserThread() # создаем поток получения списка ссылок
        self.ContentListParserThread_instance.finish_signal.connect(self.content_list_maker) # это финишный сигнал для возврата
        self.ContentListParserThread_instance.thread_link = self.thread_link # Передаем текст из поля для ввода (ссылку) в переменную потока
        self.ContentListParserThread_instance.start() # Стартует метод потока run
        self.processbar.setText('Done!')




    def content_list_maker(self, content_list): # Это то, что происходет опосля, после выхода из треда
        self.content_list = content_list
        


        print('всё круто, список ссылок получил')
        for link in content_list:
            print(link)
        print('на сегодня это всё, что есть')

        self.btn_download.setEnabled(True)
        
        
    def process_bar_change(self, info):
        self.info = info
        print('всё норм, количество контента из потока получил, в класс передал', self.info)
        converter = BytesConverter()
        self.processbar.setText('Всего ' + str(info.get('files')) + ' ' + rus_gramary(info.get('files')) + ', размером ' + converter.get_megabytes(info.get('total size')))        

    def inputtext_to_board_name(self, board_name):
        self.board_name = board_name
        print('всё норм, имя доски из потока получил, в класс передал', self.board_name)
        #print('Название доски: ' + board_name.get_key())
        self.input_thread.setText(board_name)

    def button_pressed(self, content_list):
        self.DownloaderThread_instance = DownloaderThread() # создаем поток
        self.DownloaderThread_instance.content_list = self.content_list # Передаем текст из поля для ввода (ссылку) в переменную потока
        self.DownloaderThread_instance.start() # Стартует метод потока run

        #self.downloading(self.content_list)
        
'''
    def downloading(self, content_list):
        simple_async_downloader.sync_runner(self.content_list)
        print('метод скачивания закончил!')
'''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    desktop = app.primaryScreen()
    #desktop = QApplication.desktop()
    

    window_width = 526  # ширина окна
    window_height = 120 # высота окна
    desktop_width = desktop.size().width() # ширина стола
    desktop_height = desktop.size().height() # высота стола

    #print('ширина стола', desktop_width)
    #print('высота стола', desktop_height)
    #print('ширина окна', window_width)
    #print('высота окна', window_height)
    
    window = QWidget()
    window.resize(window_width, window_height)
    
    pos_X_coordinate = get_window_center(desktop_width, window_width)
    pos_Y_coordinate = get_window_center(desktop_height, window_height)
    #print('Х-координата верхней левой точки', pos_X_coordinate)
    #print('У-координата верхней левой точки', pos_Y_coordinate)
    
    #setGeometry(X co-ordinate, Y co-ordinate, Width of the window to be set, Height of the window to be set)
    window.setGeometry(pos_X_coordinate, pos_Y_coordinate, window_width, window_height)

    screen = QMainWindow()
    
    
    #screen.resize(window_width, window_height)

    screen.setGeometry(pos_X_coordinate, pos_Y_coordinate, window_width, window_height)
    
    screen.show()

    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec_())