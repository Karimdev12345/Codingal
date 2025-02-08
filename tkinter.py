from tkinter import *
#from datetime import date

root= Tk()
root.title ('Getting Started With Widges')
root.geometry('400x300')

lbl= Label(text= "Hey There!", fg= "white", bg= "black", height= 100, width= 300)

name_lbl= Label(text= "Full Name", bg= "white")
name_entry= Entry()

root.mainloop()

