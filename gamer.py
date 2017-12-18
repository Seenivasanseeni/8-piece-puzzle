grid=[[0]*3 for i in range(3)]

def prettyPrint():
	print("====================================")
	global grid
	for i in range(3):
		print(grid[i])
	print("=====================================")

prettyPrint()
print("grid made with zeros")

def makeGrid():
	global grid
	#curently static arrangement
	grid=[[7,3,5],[6,8,1],[4,2,0]]

makeGrid()
prettyPrint()
print("Grid made")

#define moves
moves={"UP":(-1,0),"DOWN":(1,0),"LEFT":(0,-1),"RIGHT":(0,1)}

#zero position
i,j=2,2

def getmoves():
	valid_moves=[]
	for move in moves:
		ii=i
		jj=j
		ii+=moves[move][0]
		jj+=moves[move][1]
		if(ii>=0 and ii<3 and jj>=0 and jj<3):
			valid_moves.append(move)
	return valid_moves

while True:
	#get the possible moves
	valid_moves=getmoves()
	print(valid_moves)

	#get a move from the user
	selected_move=input("Enter Move: ")
	try:
		ii=i+moves[selected_move][0]
		jj=j+moves[selected_move][1]
		grid[i][j]=grid[ii][jj]
		i=ii
		j=jj
		grid[i][j]=0
	except:
		print("Invalid Move.Check Your spelling and Capitalization")

	prettyPrint()
