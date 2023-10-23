class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for i, n in enumerate(nums):
            req  = target - n
            if req in map:
                return [i, map[req]]
            else:
                map[n] = i
        
        
        