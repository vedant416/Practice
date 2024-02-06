class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for i, n in enumerate(nums):
            # n + m = target
            m = target - n
            if m in map:
                return [map[m], i]
            else:
                map[n] = i  
                