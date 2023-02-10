class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        List<Integer> sol = new ArrayList<>();
        
        for( int i=0; i< nums.length ; i++ ){
            int diff = target - nums[i];
            
            for ( int j=i+1; j< nums.length; j++ ){
                
                if(nums[j] == diff){
                    sol.add(j);
                    sol.add(i);
                }
            }
        }
        
        
        return sol.stream().mapToInt(i -> i).toArray();
    }
}