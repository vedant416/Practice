
class Solution:
    def maxSubArray(self, nums):
        
        @cache
        def solve(i, must_pick):
            if i >= len(nums): 
                if must_pick:
                    return 0  
                else:
                    return -inf
                
            if must_pick:
                return max(0, nums[i] + solve(i+1, True))
            return max(solve(i+1, False), nums[i] + solve(i+1, True))
        
        return solve(0, False)        
    

    