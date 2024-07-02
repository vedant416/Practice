class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<nums[-1]:return nums[0]
        l = 0
        h = len(nums)-1
        mid = (l+h)//2
        while(l < h):
            if mid!=0 and nums[mid]<nums[mid-1]:
                return nums[mid]
            
            if nums[mid] > nums[h]:
                l = mid+1
            else:
                h = mid-1
            mid = (l+h)//2
        return nums[mid]