import tkinter as tk
from tkinter import *
from functools import partial
from random import randint

class myApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.title("Tic Tac Toe")
        self.resizable(width=False, height=False)
        self.geometry("142x47+-6+0")
        self.buttons = {}
        # turn -1 is first player turn, 1 is second player turn or ai turn
        self.turn = -1
        # play type selection
        self.select = Frame(self)
        self.select.grid()
        label = Label(self.select,text="How do you want to play?")
        multiplayer = Button(self.select,text="1 vs 1",command=lambda: self.start(0))
        aiEasy = Button(self.select,text="easy ai",command=lambda: self.start(1))
        ai = Button(self.select,text="hard ai",command=lambda: self.start(2))
        label.grid(row=0,column=0,columnspan=3)
        multiplayer.grid(row=1,column=0)
        aiEasy.grid(row=1,column=1)
        ai.grid(row=1,column=2)

    def start(self,mode):
        self.select.destroy()
        self.mode=mode
        self.geometry("384x384+-6+0")
        # generates buttons
        for x in range(9):
            frame = Frame(self,height=128,width=128)
            frame.pack_propagate(0)
            frame.grid(row=int(x/3),column=x%3)
            self.buttons[x] = custButton(frame)
            self.buttons[x].set("-")
            self.buttons[x].config(command=partial(self.press,x),font=("","75"))
            self.buttons[x].pack(fill=BOTH, expand=1)

    def press(self,button):
        if self.turn==1:
            try:
                self.buttons[button].set("O")
                self.buttons[button].config(state=DISABLED)
            except:
                dummy=0
        else:
            self.buttons[button].set("X")
            self.buttons[button].config(state=DISABLED)
        self.turn = self.turn * -1
        temp = self.winCheck(self.genBoard())
        if temp==-1: self.popupMsg("X wins")
        elif temp==1: self.popupMsg("O wins")
        elif temp==0: self.popupMsg("Draw")
        elif self.mode==2 and self.turn==1:
            # if ai is playng presses the button for the best move
            self.press(self.bestMove(self.genBoard()))
        elif self.mode==self.turn==1:
            self.press(self.secondBestMove(self.genBoard()))

    # runs minimax function on all available moves and returns the best one
    def bestMove(self,board):
        move,bestScore=None,-1E99
        for x in self.getMoves(board):
            tempBoard,tempBoard[x] = board.copy(),1
            score = self.minimax(tempBoard,self.turn!=1)
            if score>bestScore:
                move,bestScore=x,score
        return move

    # runs minimax function and sometimes returns the second best move
    def secondBestMove(self,board):
        move=move2=None
        bestScore=bestScore2=-1E99
        for x in self.getMoves(board):
            tempBoard,tempBoard[x] = board.copy(),1
            score = self.minimax(tempBoard,self.turn!=1)
            if score>bestScore:
                move2,bestScore2,move,bestScore=move,bestScore,x,score
            elif score>bestScore2 and score<=bestScore:
                move2,bestScore2=x,score
        if randint(0,1) and move2 is not None: return move2
        else: return move

    # recursive function that returns the value of all possible gamestates from the inputted board
    def minimax(self,board,turn):
        if self.winCheck(board) != None:
            return self.winCheck(board)
        bestVal = pow(-1,turn)*1E99
        if turn:
            for x in self.getMoves(board):
                tempBoard,tempBoard[x] = board.copy(),1
                bestVal=max(bestVal,self.minimax(tempBoard,False))
            return bestVal
        else:
            for x in self.getMoves(board):
                tempBoard,tempBoard[x] = board.copy(),-1
                bestVal=min(bestVal,self.minimax(tempBoard,True))
            return bestVal

    # generates an array to represent the game board based on the current button values
    def genBoard(self):
        board = [0]*9
        for x in range(9):
            if(self.buttons[x].get()=="X"): board[x]=-1
            if(self.buttons[x].get()=="O"): board[x]=1
        return board

    def winCheck(self,board):
        if(board[0]==board[1]==board[2] and board[0]!=0): return board[0]
        if(board[3]==board[4]==board[5] and board[3]!=0): return board[3]
        if(board[6]==board[7]==board[8] and board[6]!=0): return board[6]
        if(board[0]==board[3]==board[6] and board[0]!=0): return board[0]
        if(board[1]==board[4]==board[7] and board[1]!=0): return board[1]
        if(board[2]==board[5]==board[8] and board[2]!=0): return board[2]
        if(board[0]==board[4]==board[8] and board[0]!=0): return board[0]
        if(board[2]==board[4]==board[6] and board[2]!=0): return board[2]
        if not self.getMoves(board): return 0

    def popupMsg(self,msg):
        for x in range(9):
            self.buttons[x].config(state=DISABLED)
        self.popup = Toplevel(self)
        self.popup.title("Game Over")
        self.popup.resizable(width=False, height=False)
        self.popup.geometry("120x67+-6+0")
        label = Label(self.popup, text=msg)
        label.grid(row=0,column=0,columnspan=2, pady=10)
        B1 = Button(self.popup, text="Okay", command = self.destroy)
        B2 = Button(self.popup, text="New game", command = self.newGame)
        B1.grid(row=1,column=0, padx=(7, 0))
        B2.grid(row=1,column=1)

    def newGame(self):
        self.popup.destroy()
        self.turn = -1
        for x in range(9):
            self.buttons[x].set("-")
            self.buttons[x].config(state=NORMAL)

    # returns an array of available moves left when given a board
    def getMoves(self,board):
        return [x for x in range(9) if not board[x]]

# custom tkinter button with get and set functions
class custButton(tk.Button):
    def __init__(self,master=None,**kwargs):
        self.var = tk.StringVar()
        tk.Button.__init__(self,master,textvariable=self.var,**kwargs)
        self.get, self.set = self.var.get, self.var.set

root = myApp()
root.mainloop()
