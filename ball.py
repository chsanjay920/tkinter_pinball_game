from tkinter import *
from bat import *

class ball:
	"""docstring for Ball"""
	def __init__(self, canvas):
		self.canvas = canvas
		self.img = canvas.create_oval(100,100,50,50,fill="red")


	def move(self,xx,yy):
		self.canvas.move(self.img,xx,yy)
		
	def corr(self):
		return self.canvas.coords(self.img)