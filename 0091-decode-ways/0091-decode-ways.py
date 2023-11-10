class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(i):
            n = len(s)
            if i > n:
                return 0
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            x1 = dfs(i+1)
            x2 = 0
            
            if i+1 < len(s) and int(s[i] + s[i+1]) < 27:
                x2 = dfs(i+2)
            
            x = x1 + x2
            return x
        return dfs(0)