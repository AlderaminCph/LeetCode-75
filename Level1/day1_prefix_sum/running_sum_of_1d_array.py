"""
Given an array nums. We define a running sum of an array as runningSum[i] =
sum(nums[0]…nums[i]).

Return the running sum of nums.



Example 1:

>>> Solution().runningSum([1,2,3,4])
[1, 3, 6, 10]

Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

>>> Solution().runningSum([1,1,1,1,1])
[1, 2, 3, 4, 5]

Explanation: Running sum is obtained as follows:
[1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:

>>> Solution().runningSum([3,1,2,10,1])
[3, 4, 6, 16, 17]
"""
from typing import List
import doctest


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


doctest.testmod()
