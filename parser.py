#если поле для ввода изменилось, проверяем сразу на валидность во втором потоке
#если ссылка валидная, парсим контент сразу во втором потоке
#по нажатию кнопки останавливаем парсинг из второго потока, качаем что успело спарситься


#pip install api2ch
import api2ch
import httplib2
from urllib.parse import urlparse
import os

import asyncio
from api2ch import Api2chAsync

class Parser():
	async def get_file_count(self, thread_url: str) -> list:
		async with Api2chAsync() as api:
			valid, board, thread_id = api2ch.parse_url(thread_url)
			#print('доска', board)
			#print('тред', thread_id)
			if not valid:
				raise api2ch.Api2chError(404, 'Invalid URL')

			thread = await api.thread(board, thread_id)
			posts = thread.posts
			file_count = 0
			size_count = 0
			for post in posts:
				if post.files:
					for file in post.files:
						file_count+=1
						size_count+=file.size
			info = {'files': file_count, 'total size': size_count}
			return info

	async def get_board_name(self, thread_url: str) -> str:
		async with Api2chAsync() as api:
			valid, board, thread_id = api2ch.parse_url(thread_url)
			if not valid:
				raise api2ch.Api2chError(404, 'Invalid URL')
			thread = await api.thread(board, thread_id)
			return thread.board_name


	async def get_file_dict(self, thread_url: str) -> int:
		async with Api2chAsync() as api:
			valid, board, thread_id = api2ch.parse_url(thread_url)
			if not valid:
				raise api2ch.Api2chError(404, 'Invalid URL')
			thread = await api.thread(board, thread_id)
			file_count = 0
			posts = thread.posts
			content_list = []
			for post in posts:
				if post.files:
					for file in post.files:
						file_dict = {'link': file.url(), 'size': file.size}
						content_list.append(file_dict)
						file_count+=1
					
			return content_list

	async def get_content_list(self, thread_url: str) -> int:
		async with Api2chAsync() as api:
			valid, board, thread_id = api2ch.parse_url(thread_url)
			if not valid:
				raise api2ch.Api2chError(404, 'Invalid URL')
			thread = await api.thread(board, thread_id)
			posts = thread.posts
			links_list = []
			for post in posts:
				if post.files:
					for file in post.files:
						links_list.append(file.url())
						
			return links_list
'''
api = api2ch.Api2ch()

class Parser():
	def parse_count(self, thread_url: str) -> int:
		valid, board, thread_id = api2ch.parse_url(thread_url)
		if not valid:
			raise api2ch.Api2chError(404, 'Invalid URL')

		thread = api.thread(board, thread_id)
		posts = thread.posts
		content_count = 0
		for post in posts:
			if post.files:
				for file in post.files:
					content_count+=1

		return content_count

	def get_content_count(self, thread_url: str):
		try:
			text = self.parse_count(thread_url)
		except api2ch.Api2chError as e:
			print('Request Error', e.code, e.reason)
		else:
			return self.parse_count(thread_url)


	def get_content_data(self, url: str) -> str:
		valid, board, thread_id = api2ch.parse_url(url)
		if not valid:
			raise api2ch.Api2chError(404, 'Invalid URL')

		thread = api.thread(board, thread_id)
		posts = thread.posts
		text = ''
		content_list = []
		for post in posts:
			if post.files:
				for file in post.files:
					file_dict = {'link': file.url(), 'size': file.size}
					content_list.append(file_dict)

		return content_list

	def pretty_print_post(self, url: str):
		try:
			text = self.parse_post(url)
		except api2ch.Api2chError as e:
			print('Request Error', e.code, e.reason)
		else:
			#print(text)
			return self.parse_post(url)
'''

if __name__ == '__main__':
	thread_url = 'https://2ch.hk/wp/res/69966.html'
	content_link = 'https://2ch.hk/wp/src/69966/15882392345060.mp4'

	parser = Parser()
	print(asyncio.run(parser.get_board_name(thread_url)))

	info = asyncio.run(parser.get_file_count(thread_url))

	filelist = asyncio.run(parser.get_content_list(thread_url))
	print(type(filelist))
	for i in filelist:
		print(i)


	'''
	file_count = asyncio.run(parser.get_file_list(thread_url))
	print(len(file_count))
	print('---')
	for e in file_count:
		print(e)
	'''