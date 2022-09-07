class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        cols = len(grid[0])
        
        distance = {}
        queue = collections.deque()
        
        directions = [(-1,0), (0,-1), (1,0), (0,1)]
        
        for x in range(row):
            for y in range(cols):
                if grid[x][y] == 2:
                    queue.append((x,y,0))
                    distance[(x,y)] = 0
                    
        time = 0            
        while len(queue) > 0:
            x, y, d = queue.popleft()
            
            time = max(time, d)
            
            for dx, dy in directions:
                nx, ny = dx + x, dy+ y
                
                if 0 <= nx < row and 0 <= ny <cols and grid[nx][ny] == 1:
                    
                    distance[(nx,ny)] = d+1
                    grid[nx][ny] = 2 
                    queue.append((nx, ny, d +1))
                    
                    
                    
                    
        for x in range(row):
            for y in range(cols):
                if grid[x][y] == 1:
                    return -1 
                
                
        return time
        