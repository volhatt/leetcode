"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
"""

class Solution:
    #def two_sum(self, nums: List[int], target: int) -> List[int]:
    def two_sum(nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

l = [2,7,11,15]
print(Solution.two_sum(l, 9))

# output [0,1]