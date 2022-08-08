class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        {a:0, n:0, g:0, r:0, m:0}
        
        O(N) - Memory
        O(3N)- Time
        '''
        if len(s) != len(t):
            return False
        
        hashMap = {}

        for i in range(len(s)):
            if s[i] in hashMap:
                hashMap[s[i]] += 1
            else:
                hashMap[s[i]] = 1
                
        
        for i in range(len(t)):
            
            if t[i] in hashMap:
                hashMap[t[i]] -= 1
            else:
                hashMap[t[i]] = 1
                
        for index,key in enumerate(hashMap):
            
            if hashMap[key] != 0:
                return False
            
        return True
            