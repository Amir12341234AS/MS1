
from tkinter import *
import socket
ewe = input("Site =====>>>>>")
win = Tk()
win.title("site ip")
win.geometry("270x50")
win.resizable(0,0)
win.configure(background="black")
lable = Label(text="site ip:" , fg="#01DFD7", bg="black")
lable.pack(side=LEFT)
def hu():
    ford = socket.gethostbyname(ewe)
    ip_e.configure(text=ford ,  fg="white" , bg="black")
inter = Button(text="Enter ip" , fg="#01DFD7", bg="black" , command=lambda:hu())      
inter.pack()  
ip_e = Label(text="" , bg="black")
ip_e.pack(side=LEFT)
win. mainloop()

