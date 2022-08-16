class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        has_cache = [[False] * col for i in range(row)]
        cache = [[-1] * col for i in range(row)]
        
        def count(x,y):
            
            if x >= row or y >= col:
                return 0

            if obstacleGrid[x][y] == 1:
                return 0
        
            if has_cache[x][y]:
                return cache[x][y]

            if x == row-1 and y == col-1:
                return 1
            
            ways = 0
            ways += count(x + 1, y)
            ways += count(x,y + 1)
            
            has_cache[x][y] = True
            cache[x][y] = ways
            
            return ways
            
            
            
        return count(0,0)


                