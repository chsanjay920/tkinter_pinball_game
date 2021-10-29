from tkinter import *
from ball import *
from bat import *
from pynput.keyboard import Key, Listener
import time

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
def Keyboardpress(key):
	if(key.keysym == "Left"):
		bat1.bat_move_left()
	if(key.keysym == "Right"):
		bat1.bat_move_right()


win.update()
win.bind( '<Key>', lambda i : Keyboardpress(i))

def start():
	point = 0
	x,y = 2,2
	while 1:
		b1.move(x,y) 
		corrx = b1.corr()
		if corrx[1] <= 0:
			y = -y
		if corrx[2] >= 450 or corrx[0] <= 0:
			x = -x

		bcorxx = bat1.bat_corr()
		#compare coordiantes
		if abs(corrx[3]-bcorxx[3]) <= 5 and abs(corrx[0]-bcorxx[0]) <= 5:
			point += 1
			print("points : ",point)
			y = -y

		win.update()
		time.sleep(0.02)


button = Button(win,text="start",command=start)
button.place(x=75,y=50)
	
win.mainloop()


#key board listeners



