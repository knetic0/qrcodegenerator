from tkinter import *
from qr import *
import qrcode

root = Tk()
#root.geometry('100x100')
root.title('QRCODE GENERATOR')

def gui():
    Label(root, text='Please Enter a Link Here', fg='blue',font=('Arial',16)).pack()
    global link
    link = StringVar()
    linkEnt = Entry(root, textvariable=link).pack()

def qrco():
    global link
    qrc = qrcode.make(link.get())
    qrc.show()

def submit():
    submitButton = Button(root,text='Generate',font=('Arial',12),command=lambda: qrco()).pack()

gui()
submit()

root.mainloop()