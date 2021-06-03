import subprocess as sb_p
from tkinter import *

from adminlogin import *
import speech_work as sp
def Home(root,frame1):
    for frame in root.winfo_children():
        for widget in frame.winfo_children():
            widget.destroy()
    root.title("Home Page")
    Label(frame1, text="Home", font=('Helvetica', 25, 'bold'),fg="#EDF5E1",bg="#5CDB95").grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="",bg="#5CDB95").grid(row = 1,column = 0)
    speak_obj = Button(frame1, text="Start Speaking", width=15, command =lambda: sp.speak(root,frame1),bg="#05386B",fg="#EDF5E1")
    
    admin = Button(frame1, text="Admin Login", width=15, command = lambda : AdmLogin(root, frame1),bg="#05386B",fg="#EDF5E1")

    close = Button(frame1, text="Exit", width=15, command = root.destroy ,bg="#05386B",fg="#EDF5E1")

    Label(frame1, text="",bg="#5CDB95").grid(row = 2,column = 0)
    Label(frame1, text="",bg="#5CDB95").grid(row = 4,column = 0)
    Label(frame1, text="",bg="#5CDB95").grid(row = 6,column = 0)
    speak_obj.grid(row = 3, column = 1,columnspan=2)
    admin.grid(row = 5, column = 1, columnspan = 2)
    close.grid(row = 7, column = 1, columnspan = 2)
    frame1.pack()
    root.mainloop()

 
def new_home():
    root = Tk()
    root.geometry('500x500')
    root.configure(background="#5CDB95")
    frame1 = Frame(root,bg="#5CDB95")
    frame2 = Frame(root)
    Home(root, frame1)

def newWindow():
    new_home()
if __name__ == "__main__":
    new_home()
