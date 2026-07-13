from tkinter import *
def display():
    data = entry.get()
    print(data)
root = Tk()
root.geometry("300x300")
entry = Entry(root)
entry.pack()
hello = Label(root,text="Hello World", fg="red",bg="white",font=("Ariel",26))
hello.pack()

button = Button(root,text="Click Here",command=display)
button.pack()

root.mainloop()