from tkinter import *

def add():
    n1 = int(nb1.get())
    n2 = int(nb2.get())
    result= str(n1+n2)
    answer.config(text="Answer is: " + result)
root = Tk()
root.geometry("300x300")

nb1 = Entry()
nb1.pack()
nb2 = Entry()
nb2.pack()
button = Button(root,text="Add",command=add)
button.pack()

answer = Label(root)
answer.pack()
root.mainloop()