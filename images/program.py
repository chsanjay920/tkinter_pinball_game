import threading
from tkinter import *
from tkinter import messagebox
from pynput.keyboard import Key, Listener
import time
import random

class ball:
	"""docstring for Ball"""
	def __init__(self, canvas):
		self.canvas = canvas
		self.img = canvas.create_oval(100,100,50,50,fill="red")
		self.dx = random.randint(1,5)
		self.dy = random.randint(1,5)
	def move(self):
		self.canvas.move(self.img,2,2)
	def corr(self):
		return self.canvas.coords(self.img)

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

class myThread(threading.Thread):
	def __init__(self,name):
		threading.Thread.__init__(self)
		self.name = name

	def run(self):
		print ("thread started ",self.name)


class levels:
	"""docstring for levels"""
	def __init__(self):
		super(levels, self).__init__()
		self.level = 0
		self.point=0
		self.time = 0.03
		self.threads_array = []
		self.arr = []

	def incrementlevel(self,point,canvas):
		if point%5 == 0 and point>self.point:
			self.level= self.level+1
			self.arr.append(ball(canvas))
			self.time -= 0.005
			th = myThread(self.level)
			self.threads_array.append(th)
			th.start()
			if(self.time < 0):
				pass

		self.point = point

win = Tk()
win.title("game")
win.geometry("600x400")
sidenav = Frame(win,width="150",height="400",bg="#fadef9")
sidenav.grid(row=0,column=0)
win.resizable(False,False)
canvas = Canvas(win,width="450",height="400",bg="#ffcdc9")
canvas.grid(row=0,column=1)

b1 = ball(canvas)
bat1 = bat(canvas)
le = levels()
le.arr.append(b1)
verify_game = verifygame()

def Keyboardpress(key):
	if(key.keysym == "Left"):
		bat1.bat_move_left()
	if(key.keysym == "Right"):
		bat1.bat_move_right()

win.update()

#key board listeners
win.bind( '<Key>', lambda i : Keyboardpress(i))
p = StringVar()
l = StringVar()
def start():
	verify_game.continuegame()
	point = 0
	x,y = 2,2
	while 1:
		for ball in le.arr:
			ball.move()
		ballcord = ball.corr()
		if verify_game.gamecheck(ballcord) or verify_game.flag == 1:
			messagebox.showinfo('gameover', 'score:'+str(le.point))
			break
		if ballcord[1] <= 0:
			y = -y
		if ballcord[2] >= 450 or ballcord[0] <= 0:
			x = -x
		batcord = bat1.bat_corr()
		if ballcord[0] > batcord[0]-20 and ballcord[2] < batcord[2]+20 and abs(ballcord[3]- batcord[3]) <= 5:
			point += 1
			le.incrementlevel(point,canvas)
			# print("points : ",point)
			p.set("score : "+str(le.point))
			l.set("Level : "+str(le.level))
			y = -y

		win.update()
		time.sleep(le.time)

def stop():
	verify_game.intruptgame()

button = Button(win,text="start",width=10,command=start)
button.place(x=25,y=50)
button2 = Button(win,text="stop",width=10,command=stop)
button2.place(x=25,y=80)
label = Label( win, textvariable=l)
label.place(x=25,y=120)
label2 = Label( win, textvariable=p)
label2.place(x=25,y=150)

win.mainloop()