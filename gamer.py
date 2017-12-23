grid=[[0]*3 for i in range(3)]
grid_sol=[[1,2,3],[4,5,6],[7,8,0]]
prev_move=None
def prettyPrint():
	print("====================================")
	global grid
	for i in range(3):
		print(grid[i])
	print("=====================================")

prettyPrint()
print("grid made with zeros")

def makeGrid():
	global grid,grid_sol
	#curently static arrangement
	grid=[[8,3,5],[4,1,6],[2,7,0]]
	grid_sol=[[1,2,3],[4,5,6],[7,8,0]]
	return 2,2
def error(grid_temp):
	global grid_sol;
	count=0
	for x,y in zip(grid_temp,grid_sol):
		if(x!=y):
			count+=1
	return count

i,j=makeGrid()
prettyPrint()
print("Grid made")

#define moves
moves={"UP":(-1,0),"DOWN":(1,0),"LEFT":(0,-1),"RIGHT":(0,1)}

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


def makeInformedMoves(valid_moves,i_o,j_o):
	global grid,prev_move
	#make temporary i nadj
	min_error=1000
	min_error_move=None
	for move in valid_moves:
		i,j=i_o,j_o
		grid_temp=list([list(l) for l in grid])
		#do swap of values
		ii=i+moves[move][0]
		jj=j+moves[move][1]
		#print(grid)
		grid_temp[i][j]=grid_temp[ii][jj]
		#print(grid)
		i=ii
		j=jj
		grid_temp[i][j]=0
		#print(grid)
		error_rate=error(grid_temp)
		#print("On making ",str((ii,jj))," <>",str((i_o,j_o)),"===",str(error_rate))
		if(error_rate<min_error):
			if(prev_move=="UP" and move=="DOWN"):
				continue;
			if(prev_move=="DOWN" and move=="UP"):
				continue;
			if(prev_move=="LEFT" and move=="RIGHT"):
				continue;
			if(prev_move=="RIGHT" and move=="LEFT"):
				continue;
			min_error=error_rate
			min_error_move=move

	#select the move with in error
	selected_move=min_error_move
	print("making ",selected_move)
	i,j=i_o,j_o
	ii=i+moves[selected_move][0]
	jj=j+moves[selected_move][1]
	grid[i][j]=grid[ii][jj]
	i=ii
	j=jj
	grid[i][j]=0
	prev_move=selected_move
	return i,j

while True:
	#get the possible moves
	valid_moves=getmoves()
	print(valid_moves)

	#make a move base on the informed value of number of misposition
	i,j=makeInformedMoves(valid_moves,i,j)
	temp=input()
	prettyPrint()
