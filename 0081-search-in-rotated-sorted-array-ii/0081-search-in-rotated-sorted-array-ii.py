class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if nums == None or len(nums) == 0:
            return False
        
        lo = 0
        hi = len(nums)-1
        
        while lo <= hi:
            #remove duplicates like 3sum problem 15
            ####
            while lo < hi and nums[lo] == nums[lo+1]: lo += 1
            while lo < hi and nums[hi] == nums[hi-1]: hi -= 1
            ####
            
            # same code as 33
            mid = (lo + hi) // 2
            if nums[mid] == target : return True
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
        
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        