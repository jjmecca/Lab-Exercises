from tkinter import * # * means everything

root = Tk()  #root widget 
root.geometry("750x500") #set the window size 

myLabel = Label(root, text="Hello World", font=("Courier",30)) #going in the root widget
myLabel2 = Label(root, text="hello wordl", font=("Courier",15))
myLabel3 = Label(root, text="hELLO WOLRD", font=("Courier",10))
myLabel4 = Label(root, text="helo wordl", font=("Courier",3))

myLabel.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)
myLabel4.grid(row=4,column=2)
myLabel3.grid(row=3,column=1)

root.mainloop() #gotta get it looping/running
