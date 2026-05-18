import tkinter
canvas = tkinter.Canvas(width=1000, height=1080)
canvas.pack()
subor=open('cisla.txt','r')
x=0
for i in range(0,15):
    x=x+50
    r = subor.readline()
    r = r.strip()
    r = int(r)
    print(r)
    canvas.create_text(x,450-r*10,text=str(r))
    canvas.create_rectangle(x-25,500,x+25,500-r*10)   
subor.close()    
