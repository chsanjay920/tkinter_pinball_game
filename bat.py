from tkinter import *
class bat:
	"""docstring for bat"""
	def __init__(self, canvas):
		self.xpos=0
		self.ypos=0
		self.canvas = canvas
		self.rod = canvas.create_rectangle(5,340,95,355,fill="green")

	def bat_move_left(self):
		self.canvas.move(self.rod,-30,0)
	def bat_move_right(self):
		self.canvas.move(self.rod,30,0)

	def bat_corr(self):
		return self.canvas.coords(self.rod)