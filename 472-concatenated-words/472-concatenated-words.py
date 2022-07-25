class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        mem = {}
        hashset = set()
        
        for word in words:
            hashset.add(word)
        
        
        output = []
        
        
        def isConcat(word):
        
            
            if word in mem:
                return True
            
            for i in range(1,len(word)):
                                
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in hashset and (suffix in hashset or isConcat(suffix)):
                    mem[word] = True
                    return True
                
            return False
            
        for word in words:

            if isConcat(word):
                output.append(word)

        return output
    
    
    '''
    catdog
    
    c in set and dfs(atdog)
    ca in set and dfs(tdog)
    cat in set and dfs(dog)
    catd in set and dfs(og)
    catdo in set and dfs(g)
    
    a in set and dfs(tdog)
    at in set and dfs(dog)
    atd in set and dfs(og)
    atdo in set and dfs(g)
    
    '''