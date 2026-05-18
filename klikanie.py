import tkinter
import random
canvas = tkinter.Canvas(width=1920, height=1080)
canvas.pack()
p = 0
def gvarza():
    global gx, gy, d
    gx=random.randint(100,1820)
    gy=random.randint(100,980)
    d = random.randint(0,90)
    canvas.create_text(gx,gy,text='gvarza',angle=d,)
gvarza()

def klik(s):
    global p
    x = s.x
    y = s.y
    if x >= gx-10 and x <= gx+10 and y >= gy-10 and y <= gy+10:
        canvas.delete('all')
        gvarza()
        p = p+1
        canvas.create_text(960,540,text=p)
        if p == 20:
            exit()
canvas.bind('<Button-1>',klik)
