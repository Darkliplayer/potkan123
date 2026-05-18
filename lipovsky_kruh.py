import tkinter
import random
canvas = tkinter.Canvas(width=1920, height=1080)
canvas.pack()
p = 0
def kruh():
    gx=random.randint(0,1920)
    gy=random.randint(0,1080)
    canvas.create_oval(gx,gy,gx+50,gy+50,fill='green')
    canvas.after(10,kruh)
kruh()
def klik(event):
    canvas.delete('all')
canvas.bind('<Button-1>',klik)
