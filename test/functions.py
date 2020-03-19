class Functions:
	def add(self):
		value = int(self.display.text)
		self.display.text = str(value+1)

	def sub(self):
		value = int(self.display.text)
		self.display.text = str(value-1)
