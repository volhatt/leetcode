"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""
# import List from typing to support hinting in function definition 
from typing import List



def removeDuplicates(nums: List[int]) -> int:
    #for i in range(len(nums)-2):
    for i in nums
        print(nums[i], i)
        if nums[i] == nums[i+1]:
            del nums[i+1]
    return len(nums)

nums = [1,1,2]
print(removeDuplicates(nums))
# 2
nums = [0,0,1,1,1,2,2,3,3,4]
print(f"TEST 2 {removeDuplicates(nums)}")
# 5