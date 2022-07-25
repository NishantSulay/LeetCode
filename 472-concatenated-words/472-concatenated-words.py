class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        hashset = set()
        
        for word in words:
            hashset.add(word)
        
        
        output = []
        
        
        def isConcat(word):
            
            if word in hashset:
                return true
            
            for i in range(1,len(word)):
                                
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in hashset and (suffix in hashset or isConcat(suffix)):
                    return True
                
        
        for word in words:
            
            hashset.remove(word)
            
            if isConcat(word):
                output.append(word)
                
            hashset.add(word)
       
        return output
    