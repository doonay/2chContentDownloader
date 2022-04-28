import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.checkbox import CheckBox
from api2ch import download_thread_media
from pathlib import Path
import asyncio
from api2ch import download_thread_media

'''
Before the window is created
from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')

Dynamically after the Window was created
from kivy.core.window import Window
Window.size = (300, 100)
'''

from kivy.config import Config
Config.set('graphics', 'width', '464')
Config.set('graphics', 'height', '129')

class Screen(FloatLayout):

	def downloader(self, thread_link, str_path=None):
		if str_path != None:
			path = Path(str_path)
			download_thread_media(url=thread_link, path=path, with_thumbnails=False, skip_if_exists=True)
		else:
			download_thread_media(url=thread_link, with_thumbnails=False, skip_if_exists=True)
		print('Done!')
		self.ids.prcss_lbl.text = 'Done!'

	def info_popup(self):
		self.Settings.open()
		


class guiApp(App):
	title = '2ch media downloader'
	def build(self):
		return Screen()

if __name__ == '__main__':
    guiApp().run()
