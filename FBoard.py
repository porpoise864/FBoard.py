# Author: Sarah Oertly
# Date: 11/30/2019
# Description: Write a class named FBoard for playing a game, where player x is trying to get her piece to row 7 and
# player o is trying to make it so player x doesn't have any legal moves. It should have the following private data
# members:
#
# An 8x8 list of lists for tracking what's on each square of the board.
# A data member for tracking the game state, that holds one of the following string values: "X_WON", "O_WON", or
# "UNFINISHED".
# Data members to keep track of where the x piece is.
# The data members should all be private.
#
# An init method (constructor) that initializes the list of lists to represent an empty 8x8 board (you can use whatever
# character you want to represent empty). It should then put four o pieces on row 7, in columns 0, 2, 4, and 6. It
# should put an x piece on row 0, column 3. It should also initialize the other data members.
# A method called get_game_state, that returns the current value of game_state.
# A method called move_x that takes as parameters the row and column of the square to move to. If the desired move is
# not allowed, or if the game has already been won, it should just return false. Otherwise it should make the move and
# return true. A piece belonging to x can move 1 square diagonally in any direction. A piece is not allowed to move off
# the board or to an occupied square. If x's move gets her piece to row 7, game_state should be set to "X_WON".

# A method called move_o that takes as parameters the row and column to move from, and the row and column to move to. If
# the first pair of coordinates doesn't hold o's piece, or if the desired move is not allowed, or if the game has
# already been won, it should just return false. Otherwise it should make the move and return true. A piece belonging to
# o can move 1 square diagonally, but the row cannot increase, so any o piece has at most two available moves.
# For example, if player o has a piece at (5, 2), it could move to (4, 1) or (4, 3), but not (6, 1) or (6, 3). It is not
# allowed to move off the board or to an occupied square. If o's move leaves no legal move for x, game_state should be
# set to "O_WON".
# You do not need to track whose turn it is. Either move method can be called multiple times in a row.
#
# It doesn't matter which index of the list of lists you consider the row and which you consider the column as long as
# you're consistent.
#
# Feel free to add helper functions if you want. You may also find it useful to add a print function to help with
# debugging.

PLAYING = "PLAYING"
WAITING = "WAITING"
WINNERX = "XXXX"
WINNERO = "OOOO"
class FBoard:
    game_state = ""
    name = ""
    def _init_(self, row, column):
        self.row = row7["O"]
        self.column = column0["O"]
        self.column = column2["O"]
        self.column = column4["O"]
        self.column = column6["O"]
        self.column = column11["O"]
        self.row = row0["X"]
        self.column = column3["X"]
    def userInfo(self):
        return self.name
    def get_game_state(self):
        return self.game_state
    def set_game_state(self, row7):
        self.game_state = ["X_won"]
    def position(matrix):
        for num in range(1,7)
            print(" " + str(num) + " ", end = " ")
        print()
        for row in range(0,6):
            for col in range(0,6)
                print(" " + str(matrix[row][col]) + " ", end = " ")
            print("")
    def Matrix(row, column):
        matrix = ["*"] * row
        for i in range(row):
            matrix[i] = ["*"] * column
        return matrix
    def move_x(n):
        if n < 9 or n%3:
            return False
        c, cms, A = 1, n*n+1, [[0]*n for i in range(n)]
        for i in range(n):
            for j in range(n):
                A[i][j] = cms - c
                if i%3 == j%3 or (i+j)%3 == (n-1)%3 else c
                c += 1
        return A
    def move_o(m):
        if m < 9 or m%3:
            return False
        d, dms, B = 1, m*m+1, [[0]*m for i in range(m)]
        for i in range(m):
            for j in range(m):
                B[i][j] = dms - d
                if i%3 == j%3 or (i+j)%3 == (m-1)%3 else d
                d += 1
        return B
    def appConnect():
        userA = User("A", PLAYING)
        userB = User("B", WAITING)
        matBoard = createMatrix(6,6)
        display(matBoard)
        turn = 0
        while True:
            user = userA
                if turn%2 == 0:
                    user = userA
                    userA.set_game_state(PLAYING)
                    userB.set_game_state(WAITING)
                else:
                    user = userB
                    userB.set_game_state(PLAYING)
                    userA.set_game_state(WAITING)
                print("..................................... ")
                print("Preference : ", user.userInfo() , " SEQ : ", str(turn+1))
                print("...................................... ")
                try:
                    print( user.userInfo() , " turn >>>>>.... "
                    color = str(input("Please select X or O > "))
                    if color != 'X' and color != 'O' :
                        print("Wrong Entry", color)
                        continue
                    colNum = int(input("Please Enter column Number >"))
                        print("Wrong Entry -> Please Enter 1 - 5 : ", colNum)
                        continue
                    colNum = colNum - 1
                    for row in range(5, -1, -1):
                        if matBoard[row][colNum]=="*":
                            matBoard[row][colNum]=color
                            break
                    turn+=1
                except ValueError:
                    print('Invalid Number !! Please try again')
                display(matBoard)
                if findMatrixMatched(matBoard):
                    print(".................................. ")
                    print("User : ", user.userInfo() , " Win the match by ", str(turn/2), "steps")
                    print(".................................. ")
                    break
                if turn >= 20:
                    print("You have crossed maximum limits. Please start again.")
                    break
        if __name__ == '__main__':
            appConnect()