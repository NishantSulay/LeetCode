class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {1:1, 2:2}
        
        def climb(n):
            
            if n in memo:
                return memo[n]
            else:
                memo[n] = climb(n-1) + climb(n-2) 
                return memo[n]
            
        return climb(n)    

        
                     
      