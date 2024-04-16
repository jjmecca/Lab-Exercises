from tkinter import *
#inspired by https://www.youtube.com/watch?v=rG1SgFOzMqw

root = Tk()
root.geometry("250x250")


#establish three different frames
main_frame = Frame(root)
home_window = Frame(main_frame, height=100, width=100, 
                    pady=10, padx=10, background="white")
different_window = Frame(main_frame, height=100, width=100, 
                         pady=10, padx=10, background="yellow")

welcome_label = Label(root, text="Welcome to this Application", font=20,
                     pady=20)
welcome_label.pack()

main_frame.pack()
home_window.pack()

label_one = Label(home_window, text="I am the home window")
label_two = Label(different_window, text="I am a different window")

label_one.pack()
#pack label_two but the frame it's in isn't visible so it's not visible
label_two.pack()

#two functions to switch between the windows
#I forget one frame and one button, and raise one frame and one button
def change_window():
    home_window.forget()
    switch_button.forget()
    
    different_window.tkraise() #.tkraise is not neccessary
    return_button.tkraise()
    different_window.pack()
    return_button.pack()
    
def return_home():
    different_window.forget()
    return_button.forget()
    
    home_window.tkraise()
    switch_button.tkraise()
    home_window.pack()
    switch_button.pack()
#for project: could create two diff functions (< and >) to go back and
#forth between houses. itll forget the last house and go to the next house thru
#a list using the same variable
#establish both buttons, only pack one to begin with     
switch_button = Button(root, text="Go to new page", command=change_window)
switch_button.pack() 
return_button = Button(root, text="Return to home", command=return_home)

root.mainloop()
