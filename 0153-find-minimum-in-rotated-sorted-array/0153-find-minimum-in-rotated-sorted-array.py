class Solution:
    def findMin(self, num: List[int]) -> int:
        low, high = 0, len(num) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            if mid !=0 and num[mid-1] > num[mid]:
                return num[mid]
            if num[mid] < num[high]:
                high = mid
            elif num[mid] > num[high]:
                low = mid + 1

        return num[low]