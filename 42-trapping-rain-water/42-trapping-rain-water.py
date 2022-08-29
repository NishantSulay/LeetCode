class Solution:
    def trap(self, height: List[int]) -> int:
        
        waterSum = 0
        if len(height) < 3:
            return 0
        
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
        
        leftMax[0] = height[0]
        rightMax[len(height) - 1] = height[len(height) - 1]
        
        for i in range(1,len(height)):
            leftMax[i] = max(leftMax[i - 1], height[i])
            
        for i in reversed(range(len(height) - 1)):
            rightMax[i] = max(rightMax[i + 1], height[i])
            
        for i in range(len(height)):
            waterSum += min(leftMax[i], rightMax[i]) - height[i]
            
        return waterSum
        