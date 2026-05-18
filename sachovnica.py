import tkinter
import random
canvas = tkinter.Canvas(width=320, height=320)
canvas.pack()
x=0
y=0
k=-1
for i in range(0,8):
    for i in range(0,8):
        if k>0:
            canvas.create_rectangle(x,y,x+40,y+40,fill='white')
        else:
            canvas.create_rectangle(x,y,x+40,y+40,fill='black')
        x = x+40
        k = k*(-1)
    k = k*(-1)
    x = 0
    y = y+40
