class verifygame(object):
	"""docstring for verifygame"""
	def __init__(self):
		super(verifygame, self).__init__()
		self.flag = 0

	def gamecheck(self,ballc):
		if(ballc[1] > 350 and ballc[3] > 350):
			return True
		else:
			return False

	def intruptgame(self):
		self.flag = 1
	def continuegame(self):
		self.flag = 0
