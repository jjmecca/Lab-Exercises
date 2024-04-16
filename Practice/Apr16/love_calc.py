from tkinter import *
import random
#list of fonts https://stackoverflow.com/questions/39614027/list-available-font-families-in-tkinter
#love calculator idea from https://www.geeksforgeeks.org/love-calculator-gui-application-in-python/

root = Tk()
root.title("Love Compatibility Calculator")
root.geometry("500x400")
root.configure(background="white")

#constructing frames

#created main frame so I could place it nicely in the screen
main_frame = Frame(root, background="RosyBrown1", highlightbackground="violet red",
                   highlightcolor="violet red",
                  highlightthickness=5)
main_frame.place(x=240, y =185, anchor=CENTER)

#created three main frames for my other frames
header_frame = Frame(main_frame, height=150, background="RosyBrown1")
top_frame = Frame(main_frame, height=200, width=300, 
                    pady=10, padx=10, background="RosyBrown1",
                 borderwidth=4)
bottom_frame = Frame(main_frame, height=400, width=300, 
                         pady=5, padx=5, background="RosyBrown1",
                    borderwidth=4)

#created three sub frames to put in the top main frame
top_left = Frame(top_frame, background="RosyBrown1", pady=10, padx=10)
top_middle = Frame(top_frame)
top_right = Frame(top_frame, background="RosyBrown1", pady=10, padx=10)


header_frame.grid(row=0, column=1, columnspan=4)
top_frame.grid(row=1, column=1, columnspan=4)
bottom_frame.grid(row=2, column=1, columnspan=4)
top_left.grid(row=0, column=0)
top_middle.grid(row=0, column=1)
top_right.grid(row=0, column=2)

#in the header_frame
header_label = Label(header_frame, text="♡♡ Love Calculator ♡♡", font=("Garamond", 20),
                    background="RosyBrown1", foreground="violet red").grid(row=3)
header_text = Label(header_frame, text="Enter your name and your partner's \n name to determine your compatability", 
                    font=("Garamond", 15), background="RosyBrown1", foreground="violet red").grid(row=4)

#in the top_frame
name1=StringVar()
name1.set("")
name2=StringVar()
name2.set("")

entry_top = Entry(top_left, textvariable=name1, font=("Garamond", 12, "bold"), 
                  justify=CENTER)
label_mid = Label(top_middle, text = "+", font=25, background="RosyBrown1",
                 foreground="violet red")
entry_right = Entry(top_right, textvariable=name2, font=("Garamond", 12, "bold"), 
                  justify=CENTER)

entry_top.pack()
label_mid.pack()
entry_right.pack()

#in the bottom frame
def random_num_gen(name1, name2):
    clear_widgets()
    percent = random.randint(1,100)
    text_top =f"{name1} and {name2} are"
    text_mid =f"{percent}"
    text_bottom = "percent compatible."
    love_label_top.configure(text=text_top)
    love_label_mid.configure(text=text_mid)
    love_label_bottom.configure(text=text_bottom)
    button.configure(text="Try Another Pairing")

def clear_widgets():
    entry_top.delete(0, END)
    entry_right.delete(0, END)
    
button = Button(bottom_frame, text="Determine Your Compatibility",
               font=("Garamond", 15), background="RosyBrown1", foreground="violet red",
               command=lambda: random_num_gen(name1.get(), name2.get()))
love_label_top = Label(bottom_frame, pady=10, text="", font=("Garamond", 15), background="RosyBrown1",
                  foreground="violet red")
love_label_mid = Label(bottom_frame, text="", font=("Garamond", 30, "bold"), background="RosyBrown1",
                  foreground="violet red")
love_label_bottom = Label(bottom_frame, text="", font=("Garamond", 15), background="RosyBrown1",
                  foreground="violet red")
quit_button = Button(bottom_frame, text="Quit",font=("Garamond", 15), background="RosyBrown1", 
                    foreground="violet red", command=root.quit)

button.pack()
love_label_top.pack()
love_label_mid.pack()
love_label_bottom.pack()
quit_button.pack(pady=8)

root.mainloop()
