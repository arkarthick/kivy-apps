from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget 
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class Widgets(Widget):
	def btn(self):
		show_popup()

class Pop(FloatLayout):
	pass


class MainApp(App):
	def build(self):
		return Widgets()


def show_popup():
	win = Pop()
	popupwin = Popup(title='this in pop up window', size_hint=(None, None)
		,size=(200,200), content=win)
	popupwin.open()


if __name__ == '__main__':
	app = MainApp()
	app.run()

