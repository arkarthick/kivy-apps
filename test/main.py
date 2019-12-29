from kivy.app import App
from kivy.uix.label import Label


class KivyApp(App):
	def build(self):
		self.title = str(self.name)
		return Label(text='hello!')

if __name__ == '__main__':
	app = KivyApp()
	app.run()
