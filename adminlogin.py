import subprocess as sb_p
from tkinter import *
from Home import *
import os
from tkinter import messagebox

def showHistory(root):
    try:
     os.system('C:\\Users\\Lenovo\\Desktop\\text_work\\convo_hist.txt')   
    except:
        messagebox.showinfo("File Error ","File not Found Error")


def HomeAdmin(root,frame1):
    root.title("Admin")
    for widget in frame1.winfo_children():
        widget.destroy()
    Label(frame1, text="Admin", font=('Helvetica', 25, 'bold'),fg="#EDF5E1",bg="#5CDB95").grid(row = 0, column = 1)
    Label(frame1, text="",fg="#EDF5E1",bg="#5CDB95").grid(row = 1,column = 0)
    
    hist = Button(frame1, text="History", width=15, command = lambda: showHistory(root),bg="#05386B",fg="#EDF5E1")
    logout=Button(frame1, text="Logout", width=15, command = lambda: AdmLogin(root,frame1),bg="#05386B",fg="#EDF5E1")
    close = Button(frame1, text="Exit", width=15, command = root.destroy ,bg="#05386B",fg="#EDF5E1")
    Label(frame1, text="",fg="#EDF5E1",bg="#5CDB95").grid(row = 2,column = 0)
    Label(frame1, text="",fg="#EDF5E1",bg="#5CDB95").grid(row = 4,column = 0)
    Label(frame1, text="",bg="#5CDB95").grid(row = 6,column = 0)
    hist.grid(row = 3, column = 1, columnspan = 2)
    logout.grid(row = 5, column = 1, columnspan = 2)
    close.grid(row = 7, column = 1, columnspan = 2)
    frame1.pack()
    root.mainloop()

def log_admin(root,frame1,admin_ID,password):

    if(admin_ID.strip()=="Admin" and password=="admin"):
        HomeAdmin(root, frame1)
        
    else:
        msg = Message(frame1, text="Either ID or Password is Incorrect", width=500)
        msg.grid(row = 6, column = 0, columnspan = 5)

def AdmLogin(root,frame1):

    root.title("Admin Login")
    for widget in frame1.winfo_children():
        widget.destroy()

    root.title("Admin Login")
    Label(frame1, text="Admin Login", font=('Helvetica', 18, 'bold'),fg="#EDF5E1",bg="#5CDB95").grid(row = 0, column = 2, rowspan=1,)
    Label(frame1, text="",fg="#EDF5E1",bg="#5CDB95").grid(row = 1,column = 0) 
    Label(frame1, text="Admin ID:      ", anchor="e", justify=LEFT,fg="black",bg="#5CDB95").grid(row = 2,column = 0)
    Label(frame1, text="Password:       ", anchor="e", justify=LEFT,fg="black",bg="#5CDB95").grid(row = 3,column = 0)

    admin_ID = StringVar()
    password = StringVar()

    e1 = Entry(frame1, textvariable = admin_ID)
    e1.grid(row = 2,column = 2)
    e2 = Entry(frame1, textvariable = password, show = '*')
    e2.grid(row = 3,column = 2)

    sub = Button(frame1, text="Login", width=10, command = lambda: log_admin(root, frame1, admin_ID.get(), password.get()),bg="#05386B",fg="#EDF5E1")
    Label(frame1, text="",fg="#EDF5E1",bg="#5CDB95").grid(row = 4,column = 0,)
    sub.grid(row = 5, column = 2, columnspan = 2)

    frame1.pack()
    root.mainloop()
