class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        # divide array into consecutive subarrays of length k
        # compare total points 
        """
        [6,5,0,0]
         ^
        points  = 
        lower = 1
        upper = 5
        k = 2
        """
        points = 0 
        n = len(calories)
        
        window_total = sum(calories[:k])
        if window_total < lower:
            points -= 1
        if window_total > upper:
            points += 1
        
        for i in range(n-k):
            window_total = window_total - calories[i] + calories[i+k]
            
            if window_total < lower:
                points -= 1
            
            if window_total > upper:
                points += 1
        

                
        return points