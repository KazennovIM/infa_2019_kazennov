from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']
def new_goal(x, y, r):
	b1 = new_ball(x, y, r)
	b2 = new_ball(x, y, r / 3 * 2)
	b3 = new_ball(x, y, r / 3)
	return [b1, b2, b3]

def rnd_goal():
	return new_goal(rnd(100, 700), rnd(100, 500), rnd(50, 100))
	
def rnd_ball():
	return new_ball(rnd(100, 700), rnd(100, 500), rnd(50, 100))

def new_ball(x, y, r):
	ball = dict()
	ball['x'] = x 
	ball['y'] = y 
	ball['r'] = r 
	ball['o'] = canv.create_oval(x-r,y-r,x+r,y+r,
			fill=choice(colors), width=0)
	return ball


def click(event):
	print('click')

def move_ball(ball, dx, dy):
	ball['x'] += dx
	ball['y'] += dy
	canv.move(ball['o'], dx, dy)

def move_goal(goal, dx, dy):
	for ball in goal:
		move_ball(ball, dx, dy)

def update():
	move_goal(goal1, 1, 1)
	move_goal(goal2, -1, -1)
	root.after(10, update)

goal1 = rnd_goal()
goal2 = rnd_goal()
update()
canv.bind('<Button-1>', click)
mainloop()
