class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        '''
        1. find counts for each number O(n)
        2. sort counts by highest to lowest O(nlogn)
        3. add to set starting from highest and remove from array O(n^2)
        
        '''
        
        arr_size = len(arr)
        
        hashMap = Counter(arr)

        freq = sorted(hashMap.values(), reverse=True)

        
        hash_idx = 0
        count = 0
        set_size = 0
        
        while count < arr_size//2:
            set_size += 1
            count += freq[hash_idx]
            
            hash_idx += 1
            
        return set_size
        