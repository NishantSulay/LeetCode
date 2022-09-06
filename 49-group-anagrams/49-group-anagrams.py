class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grouped = collections.defaultdict(list)
        
        def normalized(word):
            return "".join(sorted(word))
        
        for word in strs:
            grouped[normalized(word)].append(word)
            
        return grouped.values()    
            
        