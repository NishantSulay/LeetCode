class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        queue = []
        visited = set()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '*':
                    queue.append((i,j,0))
                    visited.add((i,j))
                    
                    break
                    
        
        directions = [[-1,0],[1,0],[0,-1],[0,1]] 
        
        while queue:
            cur_row, cur_col, steps = queue.pop(0)
            if grid[cur_row][cur_col] == '#':
                return steps
            else:
                for dir in directions:
                    next_row = cur_row + dir[0]
                    next_col = cur_col + dir[1]
                    
                    if (0 <= next_row < rows) and (0 <= next_col < cols) and grid[next_row][next_col] != 'X' :
                        if (next_row, next_col) not in visited:
                            queue.append((next_row, next_col, steps+1))
                            visited.add((next_row, next_col))
                        
                        
            
        return -1    
        
            