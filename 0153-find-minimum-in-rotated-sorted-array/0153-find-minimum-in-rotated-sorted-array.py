class Solution:
    def findMin(self, num: List[int]) -> int:
        low, high = 0, len(num) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            if num[mid] < num[high]:
                high = mid
            elif num[mid] > num[high]:
                low = mid + 1

        return num[low]