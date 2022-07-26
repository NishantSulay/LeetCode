class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        output = 0 
        
    
        def dfs(grid, row, col):
            
             
            # out of bounds
            if(row < 0 or row > len(grid)-1):
                return
            if(col < 0 or col > len(grid[0])-1):
                return
            
            # already visited or not an island 
            if(grid[row][col] == "0"):
                return
            
            
            # mark this cell as visited
            
            
            grid[row][col] = "0"
            
            #Check adjacent cells
            dfs(grid, row, col-1)
            dfs(grid, row, col+1)    
            dfs(grid, row-1,col)
            dfs(grid, row+1,col)
    
            
            
            
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == "1"):
                    output += 1
                    dfs(grid, i,j)
                
                
                
        return output
    