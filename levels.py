class levels:
	"""docstring for levels"""
	def __init__(self):
		super(levels, self).__init__()
		self.level = 0
		self.point=0
		self.time = 0.02563145

	def incrementlevel(self,point):
		if point%5 == 0 and point>self.point:
			self.level= self.level+1
			self.time -= 0.005
		self.point = point

	



		