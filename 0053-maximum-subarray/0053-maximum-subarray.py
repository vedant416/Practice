
class Solution:
    def maxSubArray(self, nums):
        
        @cache
        def solve(i, must_pick):
            if i >= len(nums): 
                if must_pick:
                    return 0  
                else:
                    return -inf
            
            choice1 = nums[i] + solve(i+1, True)
            if must_pick:
                return max(0, choice1)
            choice2 = solve(i+1, False)
            
            return max(choice1, choice2)
        
        return solve(0, False)        
    