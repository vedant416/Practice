```
def removeDuplicates(nums,k):
if len(nums) < k: return len(nums)
slow = fast = k
while fast < len(nums):
if nums[slow - k] == nums[fast]:
fast += 1
else:
nums[slow] = nums[fast]
fast += 1
slow += 1
nums = nums[:slow]
print(nums)
​
​
nums = [ 1,1,1,1,2,2,2,2,3,3,3,3]
removeDuplicates(nums,3)
```