from tkinter import *
HEIGHT = 500
WIDTH = 800
window = Tk()
window.title('Stoppa bubblorna')
window.minsize(WIDTH, HEIGHT)
window.maxsize(WIDTH, HEIGHT)
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='darkblue')
c.pack()
ship_id = c.create_polygon(5,5,5,25,30,15,fill='red')
ship_id2 = c.create_oval(0,0,30,30, outline='red')
SHIP_R = 15
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
c.move(ship_id, MID_X, MID_Y)
c.move(ship_id2, MID_X, MID_Y)
