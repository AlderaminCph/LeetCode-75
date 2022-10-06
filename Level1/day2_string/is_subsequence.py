"""
Given two strings s and t, return true if s is a subsequence of t, or false
otherwise.

A subsequence of a string is a new string that is formed from the original
string by deleting some (can be none) of the characters without disturbing
the relative positions of the remaining characters. (i.e., "ace" is a
subsequence of "abcde" while "aec" is not).



Example 1:

>>> Solution().isSubsequence("abc","ahbgdc")
True

Example 2:

>>> Solution().isSubsequence("axc","ahbgdc")
False
"""
import doctest


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i <= len(s) - 1 and j <= len(t) - 1:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i != len(s):
            return False
        return True


doctest.testmod()
