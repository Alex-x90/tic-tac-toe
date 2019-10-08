import tkinter as tk
from tkinter import *
from functools import partial

class myApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.title("Tic Tac Toe")
        self.resizable(width=False, height=False)
        self.buttons = {}
        self.turn = -1

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
        if self.turn==1:
            self.buttons[button].set("O")
            self.buttons[button].configure(state=DISABLED)
        else:
            self.buttons[button].set("X")
            self.buttons[button].configure(state=DISABLED)
        self.turn = self.turn * -1
        temp = self.winCheck(self.genBoard())
        if temp==-1:
            self.popupMsg("X wins")
        if temp:
            self.popupMsg("O wins")
        if temp==0:
            self.popupMsg("draw")
        if self.mode==0 and self.turn==1:
            self.press(self.bestMove(self.genBoard()))

    def bestMove(self,board):
        move=None
        score=float('-inf')
        for x in self.getMoves(board):
            tempBoard = board.copy()
            tempBoard[x]=1
            tempScore=self.minimax(board,self.turn)
            if tempScore>score:
                move=x
                score=tempScore
        return move

    def minimax(self,board,turn):
        if self.winCheck(board) != None:
            return self.winCheck(board)

        move = -1
        score = -2

        moves = self.getMoves(board)
        for x in moves:
            tempBoard = board.copy()
            tempBoard[x]= turn
            tempTurn = turn*-1
            scoreMove = -self.minimax(tempBoard,tempTurn)
            if scoreMove>score:
                score=scoreMove
                move = x

        if move==-1:
            return 0

        return score

    def genBoard(self):
        board = [0]*9
        for x in range(9):
            if(self.buttons[x].get()=="X"):
                board[x]=-1
            if(self.buttons[x].get()=="O"):
                board[x]=1
        return board

    def winCheck(self,board):
        if(board[0]==board[1]==board[2] and board[0]!=0):
            return board[0]
        if(board[3]==board[4]==board[5] and board[3]!=0):
            return board[3]
        if(board[6]==board[7]==board[8] and board[6]!=0):
            return board[6]
        if(board[0]==board[3]==board[6] and board[0]!=0):
            return board[0]
        if(board[1]==board[4]==board[7] and board[1]!=0):
            return board[1]
        if(board[2]==board[5]==board[8] and board[2]!=0):
            return board[2]
        if(board[0]==board[4]==board[8] and board[0]!=0):
            return board[0]
        if(board[2]==board[4]==board[6] and board[2]!=0):
            return board[2]

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
        self.turn = -1
        for x in range(9):
            self.buttons[x].set("-")
            self.buttons[x].configure(state=NORMAL)

    def getMoves(self,board):
        output = []
        for x in range(9):
            if board[x]==0:
                output.append(x)
        return output

class custButton(tk.Button):
    def __init__(self,master=None,**kwargs):
        self.var = tk.StringVar()
        tk.Button.__init__(self,master,textvariable=self.var,**kwargs)
        self.get, self.set = self.var.get, self.var.set

root = myApp()
root.mainloop()
