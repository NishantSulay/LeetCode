class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
        Set<List<Integer>> ans = new HashSet<>();
        int length = nums.length;
        
        Arrays.sort(nums);
        
        for (int i=0; i<length -2; i++){
            int target = nums[i] * -1;
            
            int left = i+1;
            int right = length-1;
            
            while(left < right){
                if(nums[left] + nums[right] < target ){
                    left++;
                    
                } else if(nums[left] + nums[right] > target) {
                    right--;
                    
                } else {

                    
                    ans.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    right--;
                    
                }
            }
        }
        
        return new ArrayList<>(ans);
        
    }
}

/*

Sort the array first and then set element as the -1*target and the rest of the array
as a 2-sum problem
[-4,-1,-1,0,1,2]
target = 1
[-1,0,1,2]
a = -1
b = 2

[-1,-1,2]


target = 1
[0,1,2]
a = 0
b = 1

[-1,0,1]

Sort the array first and then set element as the -1*target. Use 2 pointers for the rest of the array. If l+r is smaller than target then l+1 else r-1. 
[-4,-1,-1,0,1,2]

target = 1
[-1,0,1,2]
  L
        R
L = -1
R = 2

time = O(n) + O(nlogn) = O(n)
space = O(1)
*/