class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [] 
        
        # [-1, 1, 0, -3, 3]
        #            
        # [1, -1, -1, 0, 0]
        # [0, 0, -9, 3, 1]
        #
        # [0, 0, 9, 0, 0]
        
        
        # 2 for loop passes 
        # 1 for loop for prodct of left and right pass
        
        leftProd = [0] * len(nums)
        leftProd[0] = 1
        for i in range(1,len(nums)):
            leftProd[i] = leftProd[i-1] * nums[i-1]
            
        rightProd = [0] * len(nums)
        rightProd[len(nums)-1] = 1
        for i in reversed(range(len(nums)-1)):
            rightProd[i] = rightProd[i+1] * nums[i+1]
            
        
        for i in range(len(nums)):
            output.append( leftProd[i] * rightProd[i])
            
        
        return output 
    
            
            