from tkinter import *
from ball import *
from bat import *
from levels import *
from verifygame import *
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
le = levels()
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
		b1.move(x,y) 
		ballcord = b1.corr()
		if verify_game.gamecheck(ballcord) or verify_game.flag == 1:
			break
		if ballcord[1] <= 0:
			y = -y
		if ballcord[2] >= 450 or ballcord[0] <= 0:
			x = -x
		batcord = bat1.bat_corr()
		if ballcord[0] > batcord[0]-20 and ballcord[2] < batcord[2]+20 and abs(ballcord[3]- batcord[3]) <= 5:
			point += 1
			le.incrementlevel(point)
			print("points : ",point)
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





