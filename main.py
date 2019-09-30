import tkinter as tk
from tkinter import *
from functools import partial

class custButton(tk.Button):
    def __init__(self,row,col,master=None,**kwargs):
        self.var = tk.StringVar()
        tk.Button.__init__(self,master,textvariable=self.var,**kwargs)
        self.row=row
        self.col=col
        self.get, self.set = self.var.get, self.var.set
    def press(self,mode):
        print(str(self.row)+" "+str(self.col)+" "+str(mode))

def game(mode):
    for i in range(3):
        for j in range(3):
            frame = Frame(root,height=128,width=128)
            frame.pack_propagate(0)
            frame.grid(row=i,column=j)
            button = custButton(i,j,frame)
            button.set("-")
            button.configure(command=partial(button.press, mode),font=("","75"))
            frame.grid(row=i,column=j)
            button.pack(fill=BOTH, expand=1)

def start(mode,select):
    select.destroy()
    game(mode)

root = Tk()
root.title("Tic Tac Toe")
root.resizable(width=False, height=False)

select = Frame(root)
select.grid()

label = Label(select,text="How do you want to play?")
multiplayer = Button(select,text="1 vs 1",command=lambda: start(1,select))
ai = Button(select,text="vs ai",command=lambda: start(0,select))
label.grid(row=0,column=0,columnspan=2)
multiplayer.grid(row=1,column=0)
ai.grid(row=1,column=1)

root.mainloop()
