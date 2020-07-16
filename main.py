#new python file to create sudoku file
#testing to make sure that github is working
board = [
	[7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo):
	for i in range(len(bo)):
		if not (i % 3) and i != 0:
			print("- - - - - - - - - - - - -") # horizontal line in order to separate the 9x9 blocks of numbers

		for j in range(len(bo[0])):
			if not( j % 3 ):
				print(" | ", end="") # vertical line for same purpose, end = "" makes sure that the print statement does not include a \n

			if j == 8:
				print(bo[i][j]) #ensure that the \n is included
			else:
				print(str(bo[i][j]) + " ", end="")

print_board(board)