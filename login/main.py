from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

from os import listdir
path = '.\\kv_files\\'
for file in listdir(path):
	Builder.load_file(path+file)

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '250')

class LoginPage(BoxLayout):
	pass

class MainPAge(BoxLayout):
	pass

class MainApp(App):
	def build(self):
		return LoginPage()


if __name__ == '__main__':
	app = MainApp()
	app.run()