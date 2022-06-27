import os

class FileManager():
	'''
		try:
			os.mkdir(fulldirname)
		except FileExistsError: #[WinError 183] Невозможно создать файл, так как он уже существует
			pass
	'''
	def get_path(self, path=os.getcwd()):
		return path

	def get_short_dirname(self, link): # на вход принимает хоть ссылку на тред, хоть ссылку на контент - выход одинаковый
		path = os.path.dirname(link)
		return os.path.split(path)[-1]

	def get_short_filename(self, content_link):
		return os.path.basename(content_link)

	def get_full_dirname(self, link): # на вход принимает хоть ссылку на тред, хоть ссылку на контент - выход одинаковый
		return os.path.join(self.get_path(), self.get_short_dirname(link))

	def get_full_filename(self, content_link):
		return os.path.join(self.get_path(), self.get_short_dirname(content_link), self.get_short_filename(content_link))
	
	def directory_maker(self, content_link):
		full_dirname = self.get_full_dirname(content_link)
		if os.path.exists(full_dirname):
			print('Directory', self.get_short_dirname(content_link), 'already exist.')
		else:
			os.mkdir(full_dirname)
			print('Directory', self.get_short_dirname(content_link), 'created.')


if __name__ == '__main__':

	thread_url = 'https://2ch.hk/wp/res/69966.html'
	content_link = 'https://2ch.hk/wp/src/69966/16526279552690.jpg'
	filemanager = FileManager()
	print('path', filemanager.get_path())
	print('short_dirname', filemanager.get_short_dirname(content_link))
	print('short_filename', filemanager.get_short_filename(content_link))
	print('full_dirname', filemanager.get_full_dirname(content_link))
	print('full_filename', filemanager.get_full_filename(content_link))
	print('short_dirname_from_thread_url', filemanager.get_short_dirname(thread_url))
	print('short_dirname', filemanager.get_short_dirname(thread_url))
	print('short_dirname_from_thread_url', filemanager.get_short_dirname(thread_url))
	print('short_dirname', filemanager.get_short_dirname(thread_url))
	#filemanager.directory_maker(content_link)
