class Solution:
    def findMin(self, num: List[int]) -> int:
        low, high = 0, len(num) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            
            # 4 5 6 0 1 2 3
            # L     M     R
            if mid !=0 and num[mid - 1] > num[mid]:
                return num[mid]
            
            # 4 5 6 0 1 2 3
            # L       M   R
            if num[mid] < num[high]:
                high = mid
            
            # 4 5 6 0 1 2 3
            # L   M       R
            elif num[mid] > num[high]:
                low = mid + 1

        return num[low]