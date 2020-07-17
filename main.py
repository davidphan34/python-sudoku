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

def solve(bo):
	

def valid(bo, num, pos):

	#check row
	for i in range(len(bo[0])):
		#pos[0] is the row tuple
		#checks every number in board and compares it to num to see if it's valid
		if bo[pos[0]][i] == num and pos[1] != i: #also skips over the position of the input value
			return False
	#checks the column
	for i in range(len(bo)):#pos[1] is the column tuple
		if bo[i][pos[1]] == num and pos[0] != i:
			return False

	#determine the 3x3 box that we're in
	#boxes will be identified by x,y value
	box = []
	box[0] = pos[1] // 3 #box x value
	box[1] = pos[0] // 3 #box y value

	for i in range(box[1] * 3, box[1] * 3 + 3):
		for j in range(box[0] * 3, box[0] * 3 + 3):
			if bo[i][j] == num and (i,j) != pos:
				return False

	#if every check passes, return True
	return True

def print_board(bo):
	for i in range(len(bo)):
		if not (i % 3) and i != 0:
			print("- - - - - - - - - - - -") # horizontal line in order to separate the 9x9 blocks of numbers

		for j in range(len(bo[0])):
			if not( j % 3 ) and j != 0:
				print(" | ", end="") # vertical line for same purpose, end = "" makes sure that the print statement does not include a \n

			if j == 8:
				print(bo[i][j]) #ensure that the \n is included
			else:
				print(str(bo[i][j]) + " ", end="")

print_board(board)

def find_empty(bo):
	for i in range(len(bo)):
		for j in range(len(bo[0])):
			if bo[i][j] == 0:
				return (i, j) #row, col