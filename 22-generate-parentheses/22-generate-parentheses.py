class Solution:
    def generateParenthesis(self, n):
        res = []
        def dfs(leftRemain, rightRemain, path):
            if leftRemain > rightRemain or leftRemain < 0 or rightRemain < 0:
                return
            if leftRemain == 0 and rightRemain == 0:
                res.append(path)
                return
            dfs(leftRemain-1, rightRemain, path+"(")
            dfs(leftRemain, rightRemain-1, path+")")
            
        dfs(n, n, "")
        return res
        

