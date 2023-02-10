class Solution {
    public int maxProfit(int[] prices) {
        int max_profit = 0;
        int l=0, r=1;
        
        while(r < prices.length){
            
            if(prices[l] < prices[r]){
                
                int curr_profit = prices[r] - prices[l];
                if(curr_profit >= max_profit)
                    max_profit = curr_profit;               
                
            } else {
                l=r; 
            }
            r++;
        }
        
        return max_profit;
    }
}