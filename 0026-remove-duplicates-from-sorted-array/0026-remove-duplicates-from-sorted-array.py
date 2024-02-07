class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize a pointer for the unique elements
        unique_index = 0

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous unique element
            if nums[i] != nums[unique_index]:
                # Move the unique_index pointer forward
                unique_index += 1
                # Update the value at the new unique_index with the current element
                nums[unique_index] = nums[i]

        # The length of the array with duplicates removed would be (unique_index + 1)
        return unique_index + 1

        