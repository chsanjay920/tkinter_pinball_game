from tkinter import *
from tkinter import messagebox
from pynput.keyboard import Key, Listener
import time
import random

class ball:
	def __init__(self, canvas):
		self.canvas = canvas
		# self.img = canvas.create_oval(100,100,50,50,fill="red")
		self.x = random.randint(1,5)
		self.y = random.randint(1,5)
		self.x = 2
		self.y = 2

		self.topleft_x=random.randint(100,150)
		self.topleft_y=random.randint(100,150)
		self.dia=25
		self.dx=random.randint(1,5)
		self.dy=random.randint(1,5)
		self.img=canvas.create_oval(self.topleft_x,self.topleft_y,self.topleft_x+self.dia,self.topleft_y+self.dia,fill='red')

	# moving ball 
	def move(self):
		self.canvas.move(self.img,self.x,self.y)
	# get co-ordinates of ball
	def corr(self):
		return self.canvas.coords(self.img)
	
	def changeDirection(self):
		if self.corr()[1] <= 0:
			self.y = -self.y
		if self.corr()[2] >= 450 or self.corr()[0] <= 0:
			self.x = -self.x

class bat:
	def __init__(self, canvas):
		self.xpos=0
		self.ypos=0
		self.canvas = canvas
		self.rod = canvas.create_rectangle(5,340,95,355,fill="green")

	# move bat to left
	def bat_move_left(self):
		self.canvas.move(self.rod,-30,0)
	# moving bat to right
	def bat_move_right(self):
		self.canvas.move(self.rod,30,0)
	# get bat co-ordiantes
	def bat_corr(self):
		return self.canvas.coords(self.rod)

class verifygame(object):
	def __init__(self):
		super(verifygame, self).__init__()
		self.flag = 0
	# check ball co-ordiantes
	# if ball outs from range return false 
	def gamecheck(self,ballc):
		if(ballc[1] > 350 and ballc[3] > 350):
			return True
		else:
			return False

	# for breaking for loop
	def intruptgame(self):
		self.flag = 1
	# for continuing the game 
	def continuegame(self):
		self.flag = 0

class levels:
	def __init__(self):
		super(levels, self).__init__()
		self.level = 0
		self.point=0
		self.time = 0.02
		self.arr = []

	# increamenting the level in game
	def incrementlevel(self,point,canvas):
		if point%5 == 0 and point>self.point:
			self.level= self.level+1
			if self.time >= 0:
				self.time = 0.005
			else:
				self.time = self.time-0.005
			self.arr.append(ball(canvas))

		self.point = point

win = Tk()
win.title("game")
win.geometry("600x400")
win.resizable(False,False)

sidenav = Frame(win,width="150",height="400",bg="#fadef9")
sidenav.grid(row=0,column=0)

canvas = Canvas(win,width="450",height="400",bg="#ffcdc9")
canvas.grid(row=0,column=1)

b1 = ball(canvas)
bat1 = bat(canvas)
le = levels()
verify_game = verifygame()

# initiallizing variables
p = StringVar()
l = StringVar()
le.arr.append(b1)
# key board on click listeners to move bar

def Keyboardpress(key):
	if(key.keysym == "Left"):
		bat1.bat_move_left()
	if(key.keysym == "Right"):
		bat1.bat_move_right()

win.update()

#key board listeners
win.bind( '<Key>', lambda i : Keyboardpress(i))

# game starts function
def start():
	verify_game.continuegame()
	point = 0
	x,y = 2,2
	end = 0
	while 1:
		for ball in le.arr:
			ball.move()
			ball.changeDirection()
			if verify_game.gamecheck(ball.corr()) or verify_game.flag == 1:
				messagebox.showinfo('gameover', 'score:'+str(le.point))
				win.destroy
				end = 1
				break
		
			batcord = bat1.bat_corr()
			if ball.corr()[0] > batcord[0]-20 and ball.corr()[2] < batcord[2]+20 and abs(ball.corr()[3]-batcord[3]) <= 5:
				point += 1
				le.incrementlevel(point,canvas)
				# print("points : ",point)
				p.set("score : "+str(le.point))
				l.set("Level : "+str(le.level))
				ball.y = -ball.y
			win.update()
			time.sleep(le.time)
		if end == 1:
			break

# stoping the game
def stop():
	verify_game.intruptgame()

# layout designing
button = Button(win,text="start",width=10,command=start)
button.place(x=25,y=50)

button2 = Button(win,text="stop",width=10,command=stop)
button2.place(x=25,y=80)

label = Label( win, textvariable=l)
label.place(x=25,y=120)

label2 = Label( win, textvariable=p)
label2.place(x=25,y=150)

win.mainloop()
