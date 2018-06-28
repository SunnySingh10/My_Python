@@ -0,0 +1,107 @@
#Program to play Tic Tac Toe
import sys
#This function prints the broad

def print_board(board):
    print(board["top-L"] + "|" + board["top-M"] + " |" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + " |" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + " |" + board["low-R"])

#This fuctions decides when winning happens

def is_win(board):
    if(board["top-L"]==board["top-M"]==board["top-R"]!=""):
        print("You have the top row, YOU WIN!!!!")
        sys.exit()

    if (board["mid-L"] == board["mid-M"] == board["mid-R"]!=""):
        print("You have the middle row, YOU WIN!!!!")
        sys.exit()
    if (board["low-L"] == board["low-M"] == board["low-R"]!=""):
        print("You have the bottom row, YOU WIN!!!!")
        sys.exit()
    if (board["top-L"] == board["mid-L"] == board["low-L"]!=""):
        print("You have the first column, YOU WIN!!!!")
        sys.exit()
    if (board["top-M"] == board["mid-M"] == board["low-M"]!=""):
        print("You have second column, YOU WIN!!!!")
        sys.exit()
    if (board["top-R"] == board["mid-R"] == board["low-R"]!=""):
        print("You have the third column, YOU WIN!!!!")
        sys.exit()
    if (board["top-L"] == board["mid-M"] == board["low-R"]!=""):
        print("You have the diagonal, YOU WIN!!!!")
        sys.exit()
    if (board["low-L"] == board["mid-M"] == board["top-R"]!=""):
        print("You have the diagonal, YOU WIN!!!!")
        sys.exit()

#Inserts O into the board

def insert_O(value):
    if (value == "top-L"):
        board["top-L"] = "O"
    if (value == "top-M"):
        board["top-M"] = "O"
    if (value == "top-R"):
        board["top-R"] = "O"
    if (value == "mid-L"):
        board["mid-L"] = "O"
    if (value == "mid-M"):
        board["mid-M"] = "O"
    if (value == "mid-R"):
        board["mid-R"] = "O"
    if (value == "low-L"):
        board["low-L"] = "O"
    if (value == "low-M"):
        board["low-M"] = "O"
    if (value == "low-R"):
        board["low-R"] = "O"
        return (board)

#Inserts X into the board

def insert_X(value):
    if (value == "top-L"):
        board["top-L"] = "X"
    if (value == "top-M"):
        board["top-M"] = "X"
    if (value == "top-R"):
        board["top-R"] = "X"
    if (value == "mid-L"):
        board["mid-L"] = "X"
    if (value == "mid-M"):
        board["mid-M"] = "X"
    if (value == "mid-R"):
        board["mid-R"] = "X"
    if (value == "low-L"):
        board["low-L"] = "X"
    if (value == "low-M"):
        board["low-M"] = "X"
    if (value == "low-R"):
        board["low-R"] = "X"
        return (board)

board={"top-L":"", "top-M":"", "top-R":"", "mid-L":"", "mid-M":"", "mid-R":"", "low-L":"","low-M":"", "low-R":""}

i=0             #Run total of 9 times

while(i<10):

    print("Player1 please make you choice O")
    value=input()
    insert_O(value)
    print_board(board)
    is_win(board)
    i+=1
    if (i==9):
        print("Game is Tied")
        break
    print("Player2 please make you choice X")
    value1=input()
    insert_X(value1)
    print_board(board)
    is_win(board)
    i+=1
