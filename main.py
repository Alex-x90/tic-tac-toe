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
            self.buttons[x] = custButton(frame)
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
        self.turn = not self.turn
        if self.winCheck()==-1:
            self.popupMsg("X wins")
        if self.winCheck()==1:
            self.popupMsg("O wins")
        if self.winCheck()==0:
            self.popupMsg("draw")
        if self.mode==0:
            print("test")

    def winCheck(self):
        if(self.buttons[0].get()==self.buttons[1].get() and self.buttons[1].get()==self.buttons[2].get() and self.buttons[0].get()!="-"):
            if self.buttons[0].get()=="O": return 1
            else: return -1
        if(self.buttons[3].get()==self.buttons[4].get() and self.buttons[4].get()==self.buttons[5].get() and self.buttons[3].get()!="-"):
            if self.buttons[3].get()=="O": return 1
            else: return -1
        if(self.buttons[6].get()==self.buttons[7].get() and self.buttons[7].get()==self.buttons[8].get() and self.buttons[6].get()!="-"):
            if self.buttons[6].get()=="O": return 1
            else: return -1
        if(self.buttons[0].get()==self.buttons[3].get() and self.buttons[3].get()==self.buttons[6].get() and self.buttons[0].get()!="-"):
            if self.buttons[0].get()=="O": return 1
            else: return -1
        if(self.buttons[1].get()==self.buttons[4].get() and self.buttons[4].get()==self.buttons[7].get() and self.buttons[1].get()!="-"):
            if self.buttons[1].get()=="O": return 1
            else: return -1
        if(self.buttons[2].get()==self.buttons[5].get() and self.buttons[5].get()==self.buttons[8].get() and self.buttons[2].get()!="-"):
            if self.buttons[2].get()=="O": return 1
            else: return -1
        if(self.buttons[0].get()==self.buttons[4].get() and self.buttons[4].get()==self.buttons[8].get() and self.buttons[0].get()!="-"):
            if self.buttons[0].get()=="O": return 1
            else: return -1
        if(self.buttons[2].get()==self.buttons[4].get() and self.buttons[4].get()==self.buttons[6].get() and self.buttons[2].get()!="-"):
            if self.buttons[2].get()=="O": return 1
            else: return -1
        for x in range(9):
            if self.buttons[x].get()=="-":
                return
        return 0

    def popupMsg(self,msg):
        for x in range(9):
            self.buttons[x].configure(state=DISABLED)
        self.popup = tk.Tk()
        self.popup.title("Game Over")
        label = Label(self.popup, text=msg)
        label.grid(row=0,column=0,columnspan=2, pady=10)
        B1 = Button(self.popup, text="Okay", command = self.popup.destroy)
        B1.grid(row=1,column=0, padx=(7, 0))
        B2 = Button(self.popup, text="New game", command = self.newGame)
        B2.grid(row=1,column=1)
        self.popup.mainloop()

    def newGame(self):
        self.popup.destroy()
        self.turn = 0
        for x in range(9):
            self.buttons[x].set("-")
            self.buttons[x].configure(state=NORMAL)

class custButton(tk.Button):
    def __init__(self,master=None,**kwargs):
        self.var = tk.StringVar()
        tk.Button.__init__(self,master,textvariable=self.var,**kwargs)
        self.get, self.set = self.var.get, self.var.set

root = myApp()
root.mainloop()
