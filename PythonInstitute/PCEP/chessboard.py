EMPTY = "      "
ROOK = "ROOK  "
KNIGHT = "KNIGHT"
HORSE = "HORSE "
KING = "KING  "
QUEEN = "QUEEN "
WHITE_PAWN = "W PAWN"
BLACK_PAWN = "B PAWN"

board = [ [EMPTY for i in range(8)] for j in range(8) ]

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

board[0][2] = KNIGHT
board[0][5] = KNIGHT
board[7][2] = KNIGHT
board[7][5] = KNIGHT

board[0][1] = HORSE
board[0][6] = HORSE
board[7][1] = HORSE
board[7][6] = HORSE

board[0][4] = KING
board[7][3] = KING
board[7][4] = QUEEN
board[0][3] = QUEEN

board[1] = [WHITE_PAWN for x in range(8)]
board[6] = [BLACK_PAWN for x in range(8)]

print("   ", end="")
for i in range(8):
    print("______", end="   ")
print()

for rows in board:
    print(" | ", end="")
    for field in rows:
        print(field, end=" | ")
    print()
    
    print(" | ", end="")
    for i in range(8):
        print("______", end=" | ")
    print()
