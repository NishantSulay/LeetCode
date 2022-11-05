class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # time = O(n^3) | space  = 0(1)

        
        # res = []
        # nums.sort()
        # hashset = set()

        # target = 0
        # for i in range(len(nums)):
        #     target = nums[i]
        #     for j in range(i+1,len(nums)):
        #         diff = target - nums[j]
        #         if diff not in hashset:
        #             hashset.add(nums[j])
        #         else:
        #             res.append([nums[i], nums[j], diff])
        #             break
        #     hashset = set()
                   
        # return res

        nums.sort()
        res = []

        for i in range(0, len(nums)-1):
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = -1* nums[i]
            
            left = i+1
            right = len(nums)-1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left +=1
                else:
                    res.append([nums[i] ,nums[left], nums[right]])
                    left +=1 
                    while left>0 and nums[left] == nums[left-1] and left<right:
                        left +=1
                    

        return res

                 






                    