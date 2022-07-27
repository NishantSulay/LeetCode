class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        

    
    # arr = [3,1,2,4]
    # 3 can be min in only = [3] = 3*1 
    # 1 can be min in only = [1] , [1,2] , [1,2,4], [3,1] , [3,1,2] , [3,1,2,4] = 1*6
    # 2 can be min in only = [2] , [2,4] = 2* 2
    # 4 can be min in only = [4]  = 4*1 
    # sum = 3+6+4+4 = 17 
    
    # arr = [3,1,2,4]
    #( n*(n+1) )/ 2   = 10 permutations  / subarrays ; this is really poor performance wise as array length increase will lead to space and time complexity that is suboptimal
    
    # sum = number * left * right  
    
    # use monotonic stack to keep track of previous lesser than and next lesser than 
    # only add to stack if the next is greater than current top else pop and store index at which lesser than top  
    
        total = 0 
        stack = deque() 
        stack2 = deque()

        previous_lesser = [] 
        next_lesser = [] 
        
        previous_lesser  = [0] * len(arr)
        next_lesser = [len(arr)] * len(arr)

        stack.append(arr[0])

        # i = 3
        # [3,1,2,4]
        #         ^
        # next_lesser = [4,1,1,3]
        # previous_lesser = [-1,-1,1,2]
        # stack = [1,2]

        
        for i in range(len(arr)):
            
            while (len(stack) >1 and arr[stack[-1]] > arr[i]):
                next_lesser[stack.pop()] = i
                
            
            if len(stack) > 1:
                previous_lesser[i] = stack[-1]
            else:
                previous_lesser[i] = -1
          
            stack.append(i)

        for i in range(len(arr)):
            
            left = i - previous_lesser[i]
            right = next_lesser[i] - i
            
            total += arr[i] *left * right 

            
        mod = 10**9 + 7
        return total % mod
        
        