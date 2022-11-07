class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """
        [7,1,5,3,6,4]
           b s b s
           
        [1,2,3,4,5]
         b       s
        """
        l , r = 0, 1 
        profit = 0
        
        while r<len(prices):
            if prices[l] < prices[r]:
                profit += prices[r] - prices[l]
            
            l+=1
            r+=1
                
        return profit
                
                