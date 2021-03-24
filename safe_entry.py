from tkinter import *
import clipboard
root = Tk()
l = Label(root,text="enter your message:",padx=10,pady=10)
e = Text(root, height=4,width=50)

l.pack()
e.focus_set()
e.pack()

def myClick(self):
    text = e.get("1.0",END)
    if(text[-1] == '\n'):
        text = text[0:-2]
    if(text[-1] == '\n'):
        text = text[0:-2]
    clipboard.copy(text)
    root.destroy()

root.bind("<Shift-Return>",myClick)
myButton = Button(root,text = "submit", command=myClick)
myButton.pack()
root.mainloop()
