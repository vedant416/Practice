class Solution:
    def check(self, nums: List[int]) -> bool:
        c = 0
        for i in range(len(nums)):
            if i+1 != len(nums) and nums[i] > nums[i+1]:
                c += 1
        if nums[0] < nums[len(nums)-1]:
            c += 1
        return c <= 1
        
 