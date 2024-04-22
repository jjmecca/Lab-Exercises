#adapted from
#https://pythonassets.com/posts/hyperlink-button-in-tk-tkinter/
from tkinter import *
from tkinter.font import Font
import webbrowser


class Linkbutton(Button):

    #https://realpython.com/python-kwargs-and-args/
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(foreground="#357fde", font=("Arial", 20))
        self["cursor"] = "hand2"
        self.bind("<Enter>", self.on_mouse_enter)
        self.bind("<Leave>", self.on_mouse_leave)

    def on_mouse_enter(self, event):
        self.configure(font =("Arial", 20, "underline"))

    def on_mouse_leave(self, event):
        self.configure(font =("Arial", 20))


root = Tk()
root.title("Hyperlink in Tk")
root.geometry("400x300")
linkbutton = Linkbutton(
    text="google.com",
    command=lambda: webbrowser.open("https://google.com")
)
linkbutton.place(x=50, y=50)
root.mainloop()
