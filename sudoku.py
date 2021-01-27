#SUDOKU  SOLVER  APPLICATION#
from time import *
print("**********##########    SUDOKU SOLVER    ##########**********")
sleep(2)
grid=[]
N=9

def isValid(grid,r,c,ele):
	
	for col in range(N):
		if grid[r][col]==ele:
			return False
	
	for row in range(N):
		if grid[row][c]==ele:
			return False
	
	strtrow,strtcol=r-r%3,c-c%3
	for i in range(N//3):
		for j in range(N//3):
			if grid[i+strtrow][j+strtcol]==ele:
				return False
				
	return True
	
def displayGrid():
	for i in range(N):
		for j in range(N):
			print(grid[i][j],end=" ")
		print("\n")
		
	
def solveSudoku(grid,r,c):
	if r<N-1 and c==N:
		r+=1
		c=0
	if r==N-1 and c==N:
		return True
		
	'''if grid[r][c]<0 or grid[r][c]>N:
		return False'''
	if grid[r][c]>0:
		return solveSudoku(grid,r,c+1)
	else:
		for i in range(1,N+1):
			if(isValid(grid,r,c,i)):
				grid[r][c]=i
				if solveSudoku(grid,r,c+1):
					return True
			grid[r][c]=0
		return False

print("Hey,Hello!! I am a bot.I can solve any 3*3 sudoku!!")
print("Are you ready to give the incomplete sudoku table data???  YES  or  NO  ?? : ",end="")
while(input().upper()=="YES"):
	print("#NOTE : For any incomplete cell, give the data as 0")
	print("OK!! Give me the....")
	for i in range(0,N):
		print("Row"+str(i+1)+" data : ",end="")
		row=list(map(int,input().rstrip().split()))
		grid.append(row)
	print("----Given Data----")
	displayGrid()
	res=solveSudoku(grid,0,0)
	if res:
		print("----Sudoku Solution----")
		displayGrid()
	grid=[]
	print("Are you ready to give the incomplete sudoku table data again???  YES  or  NO  ?? : ",end="")	
print("Bye!")

