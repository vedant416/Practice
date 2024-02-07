class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        size = len(nums)
        for i in range(1, size):
            if nums[l - 1] != nums[i]:
                nums[l] = nums[i]
                l += 1
        return l 
        