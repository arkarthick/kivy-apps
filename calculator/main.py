from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from button import *
from kivy.config import Config


# Config.set()
from os import listdir
kv_path = ".\\kv_files\\"
for file in listdir(kv_path):
	Builder.load_file(kv_path+file)

class Container(GridLayout):
	def calculate(self, data):
		if data !='':
			try:
				self.display.text = str(int(eval(data)))
			except:
				self.display.text = str(data[:-1])

class MainApp(App):
	def build(self):
		return Container()


if __name__ == '__main__':
	app = MainApp()
	app.run()