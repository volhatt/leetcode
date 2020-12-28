""""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

"""
# import List from typing to support hinting in function definition 
from typing import List


class Solution:
    def runningSum(nums: List[int]) -> List[int]:
        run_sum = 0
        sum = []
        for i in range(len(nums)):
            sum.append(nums[i] + run_sum)
            run_sum += nums[i]
        return sum
        

    # test
    nums = [1,2,3,4]
   
    print(runningSum(nums))
    # expected output [1,3,6,10]
