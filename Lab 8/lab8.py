from tkinter import *
from PIL import Image, ImageTk

'''
Creating this was definitely very tedious and annoying but not too difficult.
First, I began with the basic frames which I made different colors for separation.
Creating the labels/text was all very easy, it was just making them look right 
was a bit difficult and time-consuming. I had a bit of trouble with the image, though,
with the class slides and a few searches, I was able to figure out the issue. One thing
I couldn't figure out was the lines between some buttons. I just couldn't find any simple
solutions that would look any good. I also wasn't sure if you wanted us to make any of them
buttons, being that they won't lead to anything, so I just made them labels.
'''
login = Tk()
login.geometry("600x300") 
login.title("Login")

user=Label(text="Username")
user_entry=Entry()
password=Label(text="Password")
password_entry=Entry()
submit=Button(text="Submit", command=login.destroy) #The destroy command is just for the sake of the fake facebook page

user.pack()
user_entry.pack()
password.pack()
password_entry.pack()
submit.pack()

login.mainloop()

winHeight=int(1030/1.4)
winWidth=int(1106/1.4)
root = Tk()
root.geometry(f"{winWidth}x{winHeight}") 
root.resizable(0,0)
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
    bg='white'
)

rightFrame=Frame(
    height=int(610/1.4),
    width=int(730/1.4),
    bg='white'
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

status = Label(leftFrame, text="           Status                                           edit ", fg='#3a599a',bg='#d7dfe7',)
status.place(anchor='center', relx=0.47, rely=0.96)

title = Label(topFrame,text='facebook', fg='white',bg='#3a599a',font=('Arial',25,'bold'))
title.place(anchor=NW, relx=0.01, rely=0.1)

profile = Label(top2_Frame,text="Matt Cahill's Profile (This is you)", fg='white',bg='#6f83b6',font=('Arial',15,'bold'))
profile.place(anchor=NW, relx=0.01, rely=0.04)

title2 = Label(top2_Frame,text="Facebook", fg='white',bg='#6f83b6',font=('Arial',15,'bold'))
title2.place(anchor=NE, relx=0.99, rely=0.04)

menu_options = Label(topFrame,text="home        search        browse        share        invite        help        logout", fg='#b5c5dd',bg='#3a599a',font=('Arial',13))
menu_options.place(anchor=NE, relx=0.98, rely=0.25)

name=Label(rightTopFrame, text="Matt Cahill",fg="#586595",bg="white",font=('Arial', 18, 'bold'))
name.place(anchor=NW, relx=0.01, rely=0.04)

facebook=Label(rightTopFrame, text="Facebook",fg="#534a41",bg='white',font=('Arial', 13,'bold'))
facebook.place(anchor=NW, relx=0.01, rely=0.13)

school=Label(rightTopFrame,text='Iowa State Alum',fg="#534a41",bg='white',font=('Arial', 13,'bold'))
school.place(anchor=NW, relx=0.01, rely=0.205)

location=Label(rightTopFrame,text='Silicon Valley, CA',fg="#534a41",bg='white',font=('Arial', 13,'bold'))
location.place(anchor=NW, relx=0.01, rely=0.28)

email=Label(rightTopFrame,text='Email:',fg="#9b928b",bg='white',font=('Arial', 13))
email.place(anchor=NW, relx=0.01, rely=0.44)
email_entry=Label(rightTopFrame, text='mcahill@facebook.com',bg='white',fg='black',font=('Arial', 13))
email_entry.place(anchor=NW, relx=0.3, rely=0.44)

screenname=Label(rightTopFrame,text='AIM Screenname:',fg="#9b928b",bg='white',font=('Arial', 13))
screenname.place(anchor=NW, relx=0.01, rely=0.53)
screenname=Label(rightTopFrame,text='lacuna arcana',fg="#6f83b6",bg='white',font=('Arial', 13))
screenname.place(anchor=NW, relx=0.3, rely=0.53)

mobile=Label(rightTopFrame,text='Mobile:',fg="#9b928b",bg='white',font=('Arial', 13))
mobile.place(anchor=NW, relx=0.01, rely=0.61)
mobile=Label(rightTopFrame,text='319.378.1965',fg="black",bg='white',font=('Arial', 13,'bold'))
mobile.place(anchor=NW, relx=0.3, rely=0.61)

sex=Label(rightTopFrame,text='Sex:',fg="#9b928b",bg='white',font=('Arial', 13))
sex.place(anchor=NW, relx=0.01, rely=0.73)
sex_entry=Label(rightTopFrame,text='Male',fg="#6f83b6",bg='white',font=('Arial', 13))
sex_entry.place(anchor=NW, relx=0.3, rely=0.73)

interest=Label(rightTopFrame,text='Interested In:',fg="#9b928b",bg='white',font=('Arial', 13))
interest.place(anchor=NW, relx=0.01, rely=0.81)
interest_entry=Label(rightTopFrame,text='Women',fg="#6f83b6",bg='white',font=('Arial', 13))
interest_entry.place(anchor=NW, relx=0.3, rely=0.81)

mini_feed=Label(rightFrame,text='      Mini-feed                                                                                                         ',fg="#53679a",bg='#d8dde9',font=('Arial', 14,'bold'))
mini_feed.place(anchor=NW, relx=0, rely=0)
mini_feed=Label(rightFrame,text='      Personal Info                                                                                          edit  ',fg="#53679a",bg='#d8dde9',font=('Arial', 14,'bold'))
mini_feed.place(anchor=NW, relx=0, rely=0.065)

political=Label(rightFrame,text='Political Views:',fg="#9b928b",bg='white',font=('Arial', 13)) 
political.place(anchor=NW, relx=0.01, rely=0.14)
political_entry=Label(rightFrame,text='Moderate',fg="#6f83b6",bg='white',font=('Arial', 13)) 
political_entry.place(anchor=NW, relx=0.3, rely=0.14)

interests=Label(rightFrame,text='Interests:',fg="#9b928b",bg='white',font=('Arial', 13)) 
interests.place(anchor=NW, relx=0.01, rely=0.185)
interests_entry=Label(rightFrame,text='Web Design, Photography, Almost All Music,\nTennis, Nintendo DS Lite',fg="#6f83b6",bg='white',font=('Arial', 13),justify=LEFT) 
interests_entry.place(anchor=NW, relx=0.3, rely=0.185)

music=Label(rightFrame,text='Favorite Music:',fg="#9b928b",bg='white',font=('Arial', 13)) 
music.place(anchor=NW, relx=0.01, rely=0.27)
music_entry=Label(rightFrame,text='Zero 7, Air, Beatles, Imogen Heap, Acceptance,\nColdplay, Massive Attack, Belle & Sebastian,\nJurassic 5, Blackalicious, Björk, Scissor Sisters,\nDaft Punk, Theivery Corporation, BT, Beck,\nWilco, Deathcab for Cutie, Utada Hikaru, Way\nOut West, Radiohead, The Streets, Cake,\nChemical Brothers, Moby, Fischerspooner, High\nand Mighty Color',fg="#6f83b6",bg='white',font=('Arial', 13),justify=LEFT) 
music_entry.place(anchor=NW, relx=0.3, rely=0.27)

shows=Label(rightFrame,text='Favorite TV Shows:',fg="#9b928b",bg='white',font=('Arial', 13)) 
shows.place(anchor=NW, relx=0.01, rely=0.56)
shows=Label(rightFrame,text='Lost, Family Guy, Firefly, Bleach, Battlestar\nGalactica',fg="#6f83b6",bg='white',font=('Arial', 13),justify=LEFT) 
shows.place(anchor=NW, relx=0.3, rely=0.56)

movies=Label(rightFrame,text='Favorite Movies:',fg="#9b928b",bg='white',font=('Arial', 13)) 
movies.place(anchor=NW, relx=0.01, rely=0.65)
movies=Label(rightFrame,text="Harold and Kumar Go to White Castle, The\nIncredibles, Zoolander, Kill Bill, Ferris Bueller's\nDay Off, Fight Club, Boondock Saints, Office\nSpace, American Beauty, Stargate, Dogma,\nSuper Troopers, Wayne's World, Ocean's Eleven,\nPrimer",fg="#6f83b6",bg='white',font=('Arial', 13),justify=LEFT) 
movies.place(anchor=NW, relx=0.3, rely=0.65)

quotes=Label(rightFrame,text='Favorite Quotes:',fg="#9b928b",bg='white',font=('Arial', 13)) 
quotes.place(anchor=NW, relx=0.01, rely=0.91)
quotes=Label(rightFrame,text='"Drama is life with the dull bits cut out." -\nAlfred Hitchcock"',fg="black",bg='white',font=('Arial', 13),justify=LEFT) 
quotes.place(anchor=NW, relx=0.3, rely=0.91)

root.mainloop()