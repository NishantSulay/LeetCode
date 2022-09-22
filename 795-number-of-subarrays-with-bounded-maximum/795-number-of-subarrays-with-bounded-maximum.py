class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        
        
        '''
        [2,3,5,3]
             ^
        1 + 2 + 0 + 1     
        '''
        
        
        ans = 0
        prev = -1
        count = 0
        
        for i,num in enumerate(nums):
            if left<=num<=right:
                count = i - prev
                
            elif num>right:
                count = 0
                prev = i
                
            ans += count
    
        return ans
                
        