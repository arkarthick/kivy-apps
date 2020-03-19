from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from functions import Functions
from button import *


#load allkivy files in the folder
from os import listdir
kv_path = './kv_files/'
for kv in listdir(kv_path):
	Builder.load_file(kv_path+kv)
	

class Container(GridLayout, Functions):
	# q = ObjectProperty()
	pass


class MainApp(App):
	def build(self):
		self.title = 'kivy App'
		return Container()


if __name__ == '__main__':
	app = MainApp()
	app.run()