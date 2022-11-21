class Solution {
    public boolean containsDuplicate(int[] nums) {
        
        HashSet<Integer> map = new HashSet<Integer>();
        
        for(int i = 0; i< nums.length; i++){
            if(map.contains(nums[i])){
                return true;
            } else{
                map.add(nums[i]);
            }
        }
        
        return false;
        
    }
}