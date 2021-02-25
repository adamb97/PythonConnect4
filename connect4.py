import numpy as np
ROWCOUNT = 6
COLCOUNT = 7
def create_board():
    board = np.zeros((ROWCOUNT,COLCOUNT))
    return board


def drop_piece(board, row, col, player_piece):
	board[row][col] = player_piece

def is_valid_location(board, col):
	return board[5][col] == 0


def get_next_open_row(board, col):
	for r in range(ROWCOUNT):
		if board[r][col] == 0:
			return r
def print_board(board):
	print(np.flipud(board))

def winning_move(board, piece):
	# check horizontal locations
	for c in range(COLCOUNT-3):
		for r in range(ROWCOUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# check vertical locations
	

board = create_board()
print(board)
game_over = False
turn = 0
while not game_over:
	# player 1 input
	if turn == 0:
		column = int(input("player 1 make your selection (0-6): "))

		if is_valid_location(board, column):
			row = get_next_open_row(board, column)
			drop_piece(board, row, column, 1)



	# Player 2 input
	else:
		column = int(input("Player 2 make your selection (0-6): "))
		if is_valid_location(board, column):
			row = get_next_open_row(board, column)
			drop_piece(board, row, column, 2)
	print_board(board)
	turn +=1
	turn = turn % 2



