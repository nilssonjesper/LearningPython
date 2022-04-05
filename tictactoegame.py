import numpy as np
import weakref

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3,3))
        gameOn = True
        player = True
        round = 0
        while (gameOn == True):
            currentInput = int(input("Input field (1 - 9): ")) - 1
            row = currentInput//3
            column = currentInput%3
            if (self.board[row, column] == 0):
                if (player == True):
                    self.board[row, column] = 1
                    player = False
                    if self.checkWin() == False:
                        gameOn = False
                elif (player == False):
                    self.board[row, column] = -1
                    player = True
                    if self.checkWin() == False:
                        gameOn = False
            print(self.board)

    def __del__(self):
        print ("New Game")
        

    def checkWin(self):
        #Horizontal
        if (max(np.sum(self.board, axis=0)) == 3):
            print("Win Player One (1)")
            return False
        elif (min(np.sum(self.board, axis=0)) == -3):
            print("Win Player Two (-1)")
            return False

        #Vertikal
        if (max(np.sum(self.board, axis=1)) == 3):
            print("Win Player One (1)")
            return False
        elif (min(np.sum(self.board, axis=1)) == -3):
            print("Win Player Two (-1)")
            return False
        #Schrägen
        if (np.trace(self.board) == 3):
            print("Win Player One (1)")
            return False
        if (np.trace(self.board) == -3):
            print("Win Player Two (-1)")
            return False

        flipBoard = np.flip(self.board, axis=0)
        if (np.trace(flipBoard) == 3):
            print("Win Player One (1)")
            return False
        if (np.trace(flipBoard) == -3):
            print("Win Player Two (-1)")
            return False

    def draw(self):
        if np.absolute(self.board) == 9:
            print("Noone won")

tictactoe = TicTacToe()
while tictactoe:
    del tictactoe
    tictactoe = TicTacToe()
