from tkinter import *
from PIL import Image, ImageTk

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
    bg='white'
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

profile_picture = Canvas(leftFrame, width=250,height=430,borderwidth=0,highlightthickness = 0)
path = r"/Users/jakey/Documents/GitHub/Lab-Exercises/Lab 8/profile.png"
image = Image.open(path)
resized_image=image.resize((255,435))
photo = ImageTk.PhotoImage(resized_image)
profile_picture.create_image(0,0,image=photo,anchor=NW)
profile_picture.image = photo
profile_picture.place(relx=0.5, rely=0.35,anchor='center')

other = Label(leftFrame,text="View More Photos of Me (143)",fg='#6f83b6', bg='white')
other.place(anchor='center', relx=0.39, rely=0.71)
other = Label(leftFrame,text="Read Notes about Me (1)",fg='#6f83b6', bg='white')
other.place(anchor='center', relx=0.33, rely=0.75)
other = Label(leftFrame,text="Edit My Profile",fg='#6f83b6', bg='white')
other.place(anchor='center', relx=0.22, rely=0.79)
other = Label(leftFrame,text="Edit My Picture",fg='#6f83b6', bg='white')
other.place(anchor='center', relx=0.23, rely=0.83)
other = Label(leftFrame,text="Edit My Privacy",fg='#6f83b6', bg='white')
other.place(anchor='center', relx=0.235, rely=0.87)
other = Label(leftFrame,text="Create a Profile Badge",fg='#6f83b6', bg='white',)
other.place(anchor='center', relx=0.31, rely=0.91)

status = Label(leftFrame, text="           Status                                                    edit ", fg='#3a599a',bg='#d7dfe7',)
status.place(anchor='center', relx=0.47, rely=0.96)

title = Label(topFrame,text='facebook', fg='white',bg='#3a599a',font=('Arial',25,'bold'))
title.place(anchor=NW, relx=0.01, rely=0.1)

profile = Label(top2_Frame,text="Matt Cahill's Profile (This is you)", fg='white',bg='#6f83b6',font=('Arial',15,'bold'))
profile.place(anchor=NW, relx=0.01, rely=0.04)

title2 = Label(top2_Frame,text="Facebook", fg='white',bg='#6f83b6',font=('Arial',15,'bold'))
title2.place(anchor=NE, relx=0.99, rely=0.04)

menu_options = Label(topFrame,text="home        search        browse        share        invite        help        logout", fg='#b5c5dd',bg='#3a599a',font=('Arial',13))
menu_options.place(anchor=NE, relx=0.98, rely=0.25)

root.mainloop()