"""
Given a string s which consists of lowercase or uppercase letters, return the
length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome
here.


Example 1:

>>> Solution().longestPalindrome("abccccdd")
7

Explanation: One longest palindrome that can be built is "dccaccd",
whose length is 7.

Example 2:

>>> Solution().longestPalindrome("a")
1

Explanation: The longest palindrome that can be built is "a",
whose length is 1.
"""
from collections import defaultdict
import doctest


class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = defaultdict(int)

        for char in s:
            letters[char] += 1

        res = 0
        odd = 0

        if len(letters) == 1:
            return letters[s[0]]

        for counts in letters.values():
            if counts > 1:
                if counts % 2 == 0:
                    res += counts
                else:
                    res += counts - 1
                    odd += 1
            else:
                odd += 1

        if odd > 0:
            res += 1

        return res


doctest.testmod()
