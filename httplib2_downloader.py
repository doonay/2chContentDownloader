import time
import os
import httplib2
from filemanager import FileManager

class Simple_Downloader():
	def downloader(self, content_link, path=os.getcwd()):
		#https://2ch.hk/wp/src/69966/16526279552690.jpg 
		filename = os.path.basename(content_link)
		print('filename',filename)
		h = httplib2.Http('.cache')
		response, content = h.request(content_link)
		out = open(filename, 'wb')
		out.write(content)
		out.close()
		
if __name__ == '__main__':
	content_link = 'https://2ch.hk/wp/src/69966/15824922352511.jpg'
	
	filemanager = FileManager()
	filemanager.directory_maker(content_link)

	start = time.time()
	downloader = Simple_Downloader()
	downloader.downloader(content_link)
	end = time.time()
	print(end - start)
	
	'''
	path = content_link
	print(os.path.abspath(path), 'возвращает нормализованный абсолютный путь.')
	print(os.path.basename(path), 'базовое имя пути (эквивалентно os.path.split(path)[1]).')
	#print(os.path.commonprefix(list), 'возвращает самый длинный префикс всех путей в списке.')
	print(os.path.dirname(path), 'возвращает имя директории пути path.')
	print(os.path.exists(path), 'возвращает True, если path указывает на существующий путь или дескриптор открытого файла.')
	print(os.path.getsize(path), 'размер файла в байтах.')
	print(os.path.isabs(path), 'является ли путь абсолютным.')
	print(os.path.isfile(path), 'является ли путь файлом.')
	print(os.path.isdir(path), 'является ли путь директорией.')
	print(os.path.split(path), 'разбивает путь на кортеж (голова, хвост), где хвост - последний компонент пути, а голова - всё остальное. Хвост никогда не начинается со слеша (если путь заканчивается слешем, то хвост пустой). Если слешей в пути нет, то пустой будет голова.')
	os.path.join(path1[, path2[, ...]]) - соединяет пути с учётом особенностей операционной системы.
	'''