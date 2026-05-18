import tkinter
import random
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

entry1 = tkinter.Entry()
entry1.pack()
entry2 = tkinter.Entry()
entry2.pack()
entry3 = tkinter.Entry()
entry3.pack()

def kruh():
    x=int(entry1.get())
    y=int(entry2.get())
    r=int(entry3.get())
    c = random.choice(('blue','red','yellow','green','orange','purple'))
    canvas.create_oval(x-r,y-r,x+r,y+r,fill=c)
button1= tkinter.Button(text='kresli',command=kruh)
button1.pack()
