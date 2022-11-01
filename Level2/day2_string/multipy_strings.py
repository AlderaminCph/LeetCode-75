"""
Given two non-negative integers num1 and num2 represented as strings, return
the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs
to integer directly.



Example 1:

>>> Solution().multiply("2","3")
'6'

Example 2:

>>> Solution().multiply("123", "456")
'56088'
"""
import doctest


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = int(num1)
        num2 = int(num2)
        return str(num1 * num2)


doctest.testmod()
