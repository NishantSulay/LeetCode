class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        inverse_dict = {'(': ')', '{':'}', '[':']'}
        
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(inverse_dict.get(s[i]))
            
            else:
                if stack[-1] == s[i]:
                    stack.pop()
                else:
                    stack.append(inverse_dict.get(s[i]))
        
        return len(stack) == 0