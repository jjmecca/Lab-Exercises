from tkinter import *

winHeight=int(1030/1.4)
winWidth=int(1106/1.4)
root = Tk()
root.geometry(f"{winWidth}x{winHeight}") 
root.title("Facebook")

topFrame=Frame(
    height=int(60/1.4),
    width=int(1115/1.4),
    bg='#3a599a'
)

top2_Frame=Frame(
    height=int(40/1.4),
    width=int(1115/1.4),
    bg='#6f83b6'
)

leftFrame=Frame(
    height=int(930/1.4),
    width=int(390/1.4),
    bg='gray'
)

rightTopFrame=Frame(
    height=int(330/1.4),
    width=int(730/1.4),
    bg='green'
)

rightFrame=Frame(
    height=int(610/1.4),
    width=int(730/1.4),
    bg='blue'
)

topFrame.pack(side=TOP)
top2_Frame.pack(side=TOP)
leftFrame.pack(side=LEFT)
rightTopFrame.pack(side=TOP)
rightFrame.pack(side=RIGHT)


root.mainloop()