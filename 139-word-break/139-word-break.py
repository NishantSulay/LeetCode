class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        
        '''
        leetcode    wordDict = ["leet","code"]
        ____^ 
        l
        le
        lee
        *leet*
        leetc
        leetco
        leetcod
        
        
        applepenapple     wordDict = ["apple","pen"]
        ____^
        a
        ap
        appl
        *apple*
        
        check the rest of the string "penapple"
        
        
        O(n^n) without cache or 
        
        dogs wordDict = ["dog","s","gs"]
        ^ 
        d ogs
        do gs
        dog s

        '''
        seen = set()
        
        def checkWord(word):
            
            if word in seen:
                return False
            
            for i in range(len(word)):
                
                left = word[:i+1]
                right = word[i+1:]
                
                if left and right:
                    
                    if left in wordDict and right in wordDict:
                        return True

                    if left in wordDict and checkWord(right):
                        return True
                    
                if left and not right:
                    if left in wordDict:
                        return True
                    
                if not left and right:
                    if right in wordDict:
                        return True
            
            seen.add(word)
            return False
        
        
        return checkWord(s)
                
            
            
                
                
            
            