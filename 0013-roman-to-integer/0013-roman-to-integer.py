class Solution:
    def romanToInt(self, s: str) -> int:
        
        str_map = {'I': 1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        length = len(s)
        total = 0
        i = 0
        
        while i< len(s):
            if i+1 <= length-1 and str_map[s[i]] < str_map[s[i+1]]:
                total += str_map[s[i+1]] - str_map[s[i]]
                i += 2
            else:
                total += str_map[s[i]]
                i+= 1
            
        return total
            
                
                
            
            
            
        