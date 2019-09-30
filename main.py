import tkinter as tk
from tkinter import *

class custButton(tk.Button):
    def __init__(self,row,col,master=None,**kwargs):
        tk.Button.__init__(self,master,**kwargs)
        self.row=row
        self.col=col
    def press(self):
        print(str(self.row)+" "+str(self.col))

root = Tk()
root.title("Tic Tac Toe")
root.resizable(width=False, height=False)

for i in range(3):
    for j in range(3):
        temp = Frame(root,height=128,width=128)
        temp.pack_propagate(0)
        temp.grid(row=i,column=j)
        temp = custButton(temp,i,j,text="testing",command=temp.press)
        temp.pack(fill=BOTH, expand=1)

root.mainloop()
