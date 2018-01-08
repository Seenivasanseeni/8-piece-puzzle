import random
import queue as q
grid=[[0]*3 for i in range(3)]
grid_sol=[[1,2,3],[4,5,6],[7,8,0]]
prev_move=None
Q=q.PriorityQueue()

def prettyPrint(grid):
	print("====================================")
	for arr in grid:
		for i in range(3):
			print(arr[i],end=" ")
		print()
	print("=====================================")

def makeGrid():
	global grid,grid_sol
	#curently static arrangement
	grid=[[8,3,5],[4,1,6],[2,7,0]]
	grid=[[1,2,3],[4,5,0],[7,8,6]]
	grid_sol=[[1,2,3],[4,5,6],[7,8,0]]
	return 1,2


def man_distance(grid_temp,x,y):
	#Find xi,xj
	global grid_sol
	for arr in grid_temp:
		try:
			xj=arr.index(x)
			xi=grid_temp.index(arr)
		except:
			pass
	#find yi,yj
	for arr in grid_sol:
		try:
			yj=arr.index(y)
			yi=grid_sol.index(arr)
		except:
			pass
	return (xi-yi)*(xi-yi)+(xj-yj)*(xj-yj)

def error(grid_temp):
	global grid_sol;
	count=0
	for xa,ya in zip(grid_temp,grid_sol):
		for x,y in zip(xa,ya):
			if(x!=y):
				count+=1+man_distance(grid_temp,x,y)
	return count

#define moves
moves={"UP":(-1,0),"DOWN":(1,0),"LEFT":(0,-1),"RIGHT":(0,1)}

def getmoves(i,j):
	valid_moves=[]
	for move in moves:
		ii=i
		jj=j
		ii+=moves[move][0]
		jj+=moves[move][1]
		if(ii>=0 and ii<3 and jj>=0 and jj<3):
			valid_moves.append(move)
	return valid_moves


def makeMove(grid,i,j,valid_move):
	grid_temp=[list(l) for l in grid]
	ii=i+moves[valid_move][0]
	jj=j+moves[valid_move][1]
	grid_temp[i][j]=grid_temp[ii][jj]
	grid_temp[ii][jj]=0
	return grid_temp,ii,jj

def solve(grid_temp,i_t,j_t,depth):
	prettyPrint(grid_temp)
	error_rate=error(grid_temp)
	if(error_rate==0):
		print("Reached Goal")
		exit()
	valid_moves=getmoves(i_t,j_t)
	min_error=100000
	min_details=(0,0,0)
	for move in valid_moves:
		grid_cur,i,j=makeMove(grid_temp,i_t,j_t,move)
		error_rate=error(grid_cur)+depth
		print("error_rate:",error_rate)
		Q.put((error_rate,grid_cur,i,j,depth))

	print("In queue")
	for que in Q.queue:
		e,grid_cur,i,j,depth=que
		print(e,end=" ")
	if(not Q.empty()):
		e,grid_cur,i,j,depth=Q.get()
	print("Selected error_rate:",e)
	input()
	solve(grid_cur,i,j,depth+1)


i,j=makeGrid()
prettyPrint(grid)
print("Grid made")
solve(grid,i,j,0)