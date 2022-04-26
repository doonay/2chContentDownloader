from kivy.core.window import Window
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from PIL import Image
from kivy.properties import *

im = Image.open("accets/bg.png")
(width, height) = im.size
print(width)
print(height)

size = Window.size
print('Разрешение экрана по ширине:', type(size[0]), size[0])
print('Разрешение экрана по высоте:', type(size[1]), size[1])
print('Ширина окна приложения, как и фонового изображения:', type(width), width)
print('Высота окна приложения, как и фонового изображения:', type(height), height)
#Window.width = width
#Window.height = height
Window.size = (width, height)
print('Позиция окна приложения по х:', type(width), width)
print('Высота окна приложения по у:', type(height), height)
Window.top = width
Window.left = height

class KVBL(FloatLayout):
    wtd = NumericProperty(1)
    penrad = NumericProperty(10)
    pencolor = ListProperty([1, 0, 0, 1])  # Red
    def newclr(self, instance):
        print("Before Change@newclr: pencolor=", self.pencolor)
        self.pencolor = instance.background_color
        print("After Change@newclr: pencolor=", self.pencolor)

class KVBoxLayoutApp(App):
    def build(self):
        return KVBL()

if __name__ == '__main__':
    root = KVBoxLayoutApp()
    root.run()
