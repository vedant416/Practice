class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [ -1 for i in range(n+1)]
        def dfs(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if memo[i] != -1:
                return memo[i]
            x = dfs(i+1) + dfs(i+2)
            memo[i] = x
            return x
            
        
        return dfs(0)
        