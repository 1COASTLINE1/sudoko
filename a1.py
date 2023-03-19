"""
CSSE1001 Assignment 1
Semester 2, 2022
"""
from asyncore import read
from operator import is_
from a1_support import *


# Fill these in with your details
__author__ = "He bo yang"
__email__ ="boyang.he@uq.net.au"
__date__ = "14/07/2022"

# Write your functions here      
def num_hours() -> float:
        """
        Return the number of hours since i start to write this code
        """
        return 150.0


board_one = "68513294773459821621976485392687153485134967247325618956842739134291576819768342 "
board_two = "68513  477      1  1 764 5 9   7 5 48 1  9 724 3  6      42739  4 9   681 7   4  "
board_three = [
[6, 8, 5, 1, 3, 2, 9, 4, 7],
[7, 3, 4, 5, 9, 8, 2, 1, 6],
[2, 1, 9, 7, 6, 4, 8, 5, 3],
[9, 2, 6, 8, 7, 1, 5, 3, 4],
[8, 5, 1, 3, 4, 9, 6, 7, 2],
[4, 7, 3, 2, 5, 6, 1, 8, 9],
[5, 6, 8, 4, 2, 7, 3, 9, 1],
[3, 4, 2, 9, 1, 5, 7, 6, 8],
[1, 9, 7, 6, 8, 3, 4, 2, None]
]
board_four = [
[6, 8, 5, 1, 3, None, None, 4, 7],
[7, None, None, None, None, None, None, 1, None],
[None, 1, None, 7, 6, 4, None, 5, None],
[9, None, None, None, 7, None, 5, None, 4],
[8, None, 1, None, None, 9, None, 7, 2],
[4, None, 3, None, None, 6, None, None, None],
[None, None, None, 4, 2, 7, 3, 9, None],
[None, 4, None, 9, None, None, None, 6, 8],
[1, None, 7, None, None, None, 4, None, None]
]


def read_board(raw_board: str) -> Board:
        """
        Reads a board from a string and returns a Board object.
        """
        board1=list(raw_board)
        board2=[]
        for w in board1:
                if w == " ":
                        w = None
                        board2.append(w)
                else:    
                        w=int(w)
                        board2.append(w)
        input_array = []
        for i in range(9):
                input_array.append(board2[i*9:i*9+9])
        return input_array
def is_empty(position: tuple[int, int], board: Board) -> bool:
        """
        Returns True if the position is empty on the board.
        if board[position[0]][position[1]] == None:
                return True
        else:
                return False
        """
        h=position[0]
        b=position[1]
        if board[h][b] == None:
                return True
        else:
                return False
def update_board(position: tuple[int, int], value: Optional[int], board: Board)-> None:
        """
        Update the board at the given position with the given value.
        """
        h=position[0]
        b=position[1]
        board[h][b]=value
def clear_position(position: tuple[int, int], board: Board) -> None:
        h=position[0]
        b=position[1]
        board[h][b]=None
        return board
def print_board(board: Board)-> None:
    with open("num.txt", "w") as file:
        for i in board:
            for j in i:
                if j is None:
                    file.write(" ")
                else:
                    file.write(str(j))
            file.write("\n")

    count = 0
    with open("num.txt") as file:
        for string in file.readlines():
            string_list = list(string.rstrip())
            if len(string_list) != 9:
                for i in range(len(string_list), 9):
                    string_list.append(" ")
            string1 = string_list[0] + string_list[1] + string_list[2]
            string2 = string_list[3] + string_list[4] + string_list[5]
            string3 = string_list[6] + string_list[7] + string_list[8]
            string4 = string1 + '|' + string2 + '|' + string3 + f" {count}"
            print(string4)
            count = count + 1
            if count % 3 == 0 and count!=9:
                print("-----------")
        print("\n012 345 678")    
def has_won(board: Board) -> bool:
        """
        Returns True if the current player has won the game.
        """
        board1=[]
        board2=[]
        input_array=[]
        ans = []
        ans1 = []
        ans2 = []
        w1=0
        k=0
        w2=0
        for i in range(9):
                for j in range(9):
                        board1.append(board[i][j])
                        for x in  board1 :
                                if x not in ans:
                                        ans.append(x)
                if ans==board1 and (None not in board1):
                        w1=1
                        board1=[]
                        ans=[]
                else:
                        w1=0
                        break                                                   
        for i in range(9):
                for j in range(9):
                                board2.append(board[j][i])
                                for x in  board2 :
                                        if x not in ans1:
                                                ans1.append(x)
                if ans1 ==board2 and (None not in board2) :
                                k = 1
                                board2=[]
                                ans1=[]
                else:
                                k=0
                                break 

        for h in [0,3,6]:
                for q in [0,3,6]:
                        for i in range(h,h+3):
                                for j in range(q,q+3):
                                        input_array.append(board[i][j])
                                        for x in  input_array :
                                                if x not in ans2:
                                                        ans2.append(x)
                        if ans2 ==input_array and (None not in input_array) :
                                w2 = 1
                                input_array=[]
                                ans2=[]
                        else:
                                w2=0
                                break    
        if w1==1 and k==1 and w2==1:
                return True
                
        else:
                return False
def verification(board2: Board,check:list) -> bool:
        """
        return True if the position can be changed
        return False if the position can't be changed
        
        the first solution
        a=[]
        b=[]
        c=[]
        e=[]
        board4=[]
        for i in range(9):
                for j in range(9):
                        if board1[i][j] != None:
                                a.append(board1.index(board1[i]))
                                b=board1[i]
                                c.append(b.index(board1[i][j]))
                                e.append(board1.index(board1[i]))
                                e.append(b.index(board1[i][j]))
        range_number=len(e)//2
        for i in range(range_number):
                board4.append(e[i*2:i*2+2])
        if [check[0],check[1]] not in board4:
                return True
        else:    
                return False
        """
        #the second solution
        if is_empty((int(check[0]),int(check[1])),board2)==True:
                return True
        else:
                return False
def  main():
        board=load_board(input(START_GAME_PROMPT))
        board1=read_board(board)#board that can be changed
        original_board=read_board(board)
        print_board(original_board)
        while has_won(board1) == False:
                user_input=input(INPUT_PROMPT)
                if user_input == "H":
                        print("Need help?\nH = Help\nQ = Quit\nHint: Make sure each row, column, and square contains only one of each number from 1 to 9.\n")
                        print_board(board1)
                elif user_input == "Q":
                        break
                else:
                        input_array=user_input.split()
                        if verification(original_board,input_array) == True:
                                if input_array[2] == "C":
                                        clear_position((int(input_array[0]),int(input_array[1])),board1)
                                        print_board(board1)
                                #update_board((int(input_array[0]),int(input_array[1])),None,board1)
                                else:
                                        update_board((int(input_array[0]),int(input_array[1])),int(input_array[2]),board1)
                                        print_board(board1)
                        else:
                                print(INVALID_MOVE_MESSAGE)
                                print_board(board1)
        if has_won(board1)==True:
                print(WIN_MESSAGE)
                answer=input(NEW_GAME_PROMPT)
                if answer == "y":
                        main()
                elif answer=="n":
                        return
if __name__ == "__main__":
        main()







         



    

























