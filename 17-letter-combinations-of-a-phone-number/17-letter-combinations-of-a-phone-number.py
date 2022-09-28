class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        """
        digit = 29
        [aw, ax, ay, az, bw, bx, by, bz, cw, cx, cy, cz]
        """
        digit_mapping = {"2": ["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w","x", "y", "z"]}
        
        
        
        res = []
        
        if not digits:
            return []
        
        def backtracking(curr_idx, curr_res):
            if curr_idx >= len(digits):
                res.append("".join(curr_res))
                
            else:
                for char in digit_mapping[digits[curr_idx]]:
                    curr_res.append(char)
                    backtracking(curr_idx+1, curr_res)
                    curr_res.pop()
        
        backtracking(0, [""])
            
        
        return res
        
        