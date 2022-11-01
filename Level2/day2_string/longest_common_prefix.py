"""
Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string "".



Example 1:

>>> Solution().longestCommonPrefix(["flower","flow","flight"])
"fl"

Example 2:

>>> Solution().longestCommonPrefix(["dog","racecar","car"])
""

Explanation: There is no common prefix among the input strings.
"""
from typing import List
import doctest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        right = 1
        prefix = strs[0][0:right]
        while right < len(strs):
            for string in strs[1:]:
                if string[0:right] != prefix:
                    return ""
                else:
                    right += 1
        return prefix


doctest.testmod()
