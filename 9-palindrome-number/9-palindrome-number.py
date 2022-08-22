class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = 0
        
        if x == 0:
            return True
        
        if x<0 or x%10 == 0:
            return False
        
 
        
        while (x > result):
            tmp = x %10
            x //= 10
            result = result*10 + tmp

        return x==result or x == result//10