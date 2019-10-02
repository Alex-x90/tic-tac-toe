import tkinter as tk
from tkinter import *
from functools import partial

class myApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.title("Tic Tac Toe")
        self.resizable(width=False, height=False)
        self.buttons = {}
        self.turn = 0

        self.select = Frame(self)
        self.select.grid()
        label = Label(self.select,text="How do you want to play?")
        multiplayer = Button(self.select,text="1 vs 1",command=lambda: self.start(1))
        ai = Button(self.select,text="vs ai",command=lambda: self.start(0))
        label.grid(row=0,column=0,columnspan=2)
        multiplayer.grid(row=1,column=0)
        ai.grid(row=1,column=1)
    def start(self,mode):
        self.select.destroy()
        self.mode=mode
        for x in range(9):
            i = int(x/3)
            j = x%3
            frame = Frame(root,height=128,width=128)
            frame.pack_propagate(0)
            frame.grid(row=i,column=j)
            self.buttons[x] = custButton(i,j,frame)
            self.buttons[x].set("-")
            self.buttons[x].configure(command=partial(self.press,x),font=("","75"))
            frame.grid(row=i,column=j)
            self.buttons[x].pack(fill=BOTH, expand=1)
    def press(self,button):
        if self.turn:
            self.buttons[button].set("O")
            self.buttons[button].configure(state=DISABLED)
        else:
            self.buttons[button].set("X")
            self.buttons[button].configure(state=DISABLED)
        if self.mode:
            if self.winCheck()==0:
                print("x wins")
            if self.winCheck()==1:
                print("o wins")
            if self.winCheck()==2:
                print("draw")

        self.turn = not self.turn
    def winCheck(self):         #Doesnt work. Always returns x wins
        if(self.buttons[0].get()==self.buttons[1].get() and self.buttons[1].get()==self.buttons[2].get() and self.buttons[0].get()!="-"):
            return self.buttons[0].get()=="O"
        if(self.buttons[3].get()==self.buttons[4].get() and self.buttons[4].get()==self.buttons[5].get() and self.buttons[0].get()!="-"):
            return self.buttons[3].get()=="O"
        if(self.buttons[6].get()==self.buttons[7].get() and self.buttons[7].get()==self.buttons[8].get() and self.buttons[0].get()!="-"):
            return self.buttons[6].get()=="O"
        if(self.buttons[0].get()==self.buttons[3].get() and self.buttons[3].get()==self.buttons[6].get() and self.buttons[0].get()!="-"):
            return self.buttons[0].get()=="O"
        if(self.buttons[1].get()==self.buttons[4].get() and self.buttons[4].get()==self.buttons[7].get() and self.buttons[0].get()!="-"):
            return self.buttons[1].get()=="O"
        if(self.buttons[2].get()==self.buttons[5].get() and self.buttons[5].get()==self.buttons[8].get() and self.buttons[0].get()!="-"):
            return self.buttons[2].get()=="O"
        if(self.buttons[0].get()==self.buttons[4].get() and self.buttons[4].get()==self.buttons[8].get() and self.buttons[0].get()!="-"):
            return self.buttons[0].get()=="O"
        if(self.buttons[2].get()==self.buttons[4].get() and self.buttons[4].get()==self.buttons[6].get() and self.buttons[0].get()!="-"):
            return self.buttons[2].get()=="O"


class custButton(tk.Button):
    def __init__(self,row,col,master=None,**kwargs):
        self.var = tk.StringVar()
        tk.Button.__init__(self,master,textvariable=self.var,**kwargs)
        self.row=row
        self.col=col
        self.get, self.set = self.var.get, self.var.set

root = myApp()
root.mainloop()
