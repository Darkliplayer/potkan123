import tkinter
import random
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

entry1 = tkinter.Entry()
entry1.pack()
def kruh(s):
    x=s.x
    y=s.y
    r=int(entry1.get())
    canvas.create_oval(x-r,y-r,x+r,y+r,fill='red')
canvas.bind('<Button-1>',kruh)
