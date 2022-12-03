class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        # key(n) : value(i)
        prevMap = {}  

        for i, n in enumerate(nums):
            required = target - n
            if required in hashmap:
                return [i, hashmap[required]] 
            else:
                hashmap[n] = i
        
        
        