"""
Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string "".



Example 1:

>>> Solution().longestCommonPrefix(["flower","flow","flight"])
'fl'

Example 2:

>>> Solution().longestCommonPrefix(["dog","racecar","car"])
''

Explanation: There is no common prefix among the input strings.

>>> Solution().longestCommonPrefix(["flower","flower","flower","flower"])
'flower'

"""
from typing import List
import doctest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for string in strs:
                if i == len(string) or string[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res


doctest.testmod()
