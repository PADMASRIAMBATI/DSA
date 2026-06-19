grid = [[1,3,1],[1,5,1],[4,2,1]]
i = len(grid)
j = len(grid[0])
def fun(i,j):

    if i == 0 and j == 0:
        return grid[i][j]
    if i < 0 or j < 0:
        return float('inf')
    
    up = grid[i][j] + fun(i-1,j)
    left = grid[i][j] + fun(i,j-1)
    return min(up,left) 
print(fun(i-1,j-1))