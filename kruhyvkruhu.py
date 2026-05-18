import tkinter
import random
import math
canvas = tkinter.Canvas(width=100, height=100)
canvas.pack()

canvas.create_oval(0,0,100,100,width=5)
x = 50
y = 50
def kresli():
    global j, a, b
    a = random.randint(x-40,x+40)
    j = math.sqrt(1600-((a-50)*(a-50)))
    b = random.randint(50-int(j),50+int(j))
    canvas.create_oval(a-10,b-10,a+10,b+10,fill='red')
    canvas.after(10,kresli)
kresli()

