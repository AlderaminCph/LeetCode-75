"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the
left of the index is equal to the sum of all the numbers strictly to the
index's right.

If the index is on the left edge of the array, then the left sum is 0 because
there are no elements to the left. This also applies to the right edge of
the array.

Return the leftmost pivot index. If no such index exists, return -1.



Example 1:

>>> Solution().pivotIndex([1,7,3,6,5,6])
3

Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:

>>> Solution().pivotIndex([1,2,3])
-1

Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:

>>> Solution().pivotIndex([2,1,-1])
0

Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
"""
from typing import List
import doctest


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        pivot_index = 0
        leftsum = 0
        while pivot_index <= (len(nums) - 1):
            if pivot_index != 0:
                leftsum += nums[pivot_index - 1]
            rightsum = total - leftsum - nums[pivot_index]
            if leftsum == rightsum:
                return pivot_index
            pivot_index += 1
        return -1


doctest.testmod()
