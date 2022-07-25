class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        output = []
        
        diff = 0
        for i in range(len(nums)):
            diff = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == diff:
                    output.append(i)
                    output.append(j)
                    return output
        
      