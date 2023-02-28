class Solution:
    def climbStairs(self, n: int) -> int:
        
        '''
        0 = 0
        1 = 1
        2 = 2
        3 = 3
        4 = 1111, 112, 121, 211, 22  = 5
        5 = 11111, 1112, 1121, 1211, 2111, 212, 221, 122 = 8
        '''
        
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        last = [0] * (n)
        last[0] = 1
        last[1] = 2
        
        for i in range(2, n):
            print(i)
            last[i] = last[i-1] + last[i-2]
            
        return last[n-1]