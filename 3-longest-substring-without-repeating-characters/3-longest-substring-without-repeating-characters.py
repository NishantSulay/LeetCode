class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        N = len(s)
        
        seen = set()
        left = 0
        longest = 0
        
        for right in range(N):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                            
            seen.add(s[right])
    
            longest = max(len(seen), longest)
        
        return longest