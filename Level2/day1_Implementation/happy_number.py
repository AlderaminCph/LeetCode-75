"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the
    squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it
    loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.



Example 1:
>>> Solution().isHappy(19)
True


Example 2:

>>> Solution().isHappy(2)
False
"""
import doctest


class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sum_of_squares(n)
            if n == 1:
                return True
        return False

    def sum_of_squares(self, n: int) -> int:
        res = 0
        while n:
            digit = n % 10
            digit = digit**2
            res += digit
            n = n // 10
        return res


doctest.testmod()
