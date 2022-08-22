class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        if grid[0][0] == 1:
            return -1

    
        queue = []
        rows = len(grid)
        cols = len(grid[0])
        
        if k >= rows + cols - 2:
            return rows + cols - 2
        
        directions = [[1,0],[0,1],[0,-1],[-1,0]]       
        visited = set()
        
        state = (0,0,k)
        queue.append((0, state))
        visited.add(state)
        
        while len(queue) > 0: 
            steps, (cur_row, cur_col, remaining_k) = queue.pop(0)
            if cur_row == (rows-1) and cur_col == (cols-1):
                return steps
            
            for dir in directions:
                new_row = cur_row + dir[0]
                new_col = cur_col + dir[1]
                
                
                if (0 <= new_row < rows) and (0 <= new_col < cols):
                    
                    if grid[new_row][new_col] == 0:
                        state = (new_row, new_col, remaining_k)
                    
                    elif remaining_k>0:
                        state = (new_row, new_col, remaining_k - 1)
                        
                    else:
                        continue
                    
                    if state not in visited:
                        visited.add(state)
                        queue.append((steps+1, state))
      
        return -1 
                                
                            
                            
                
                