import tkinter
import random
canvas = tkinter.Canvas(width=1920, height=1080)
canvas.pack()

n = int(input('zadaj počet riadkov: '))
p = n
x=0
y=900
for i in range(n):
    p = p-1
    for l in range(p+1):
        c = random.choice(('blue','red','green','purple','yellow','orange'))
        canvas.create_rectangle(x,y,x+50,y+50,fill=c)
        x = x+50
    y=y-50
    x=0
    x=x+((i+1)*25)

    
    
