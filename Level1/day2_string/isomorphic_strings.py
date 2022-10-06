"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to
get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character, but a character may map to itself.



Example 1:

>>> Solution().isIsomorphic("egg","add")
True

Example 2:

>>> Solution().isIsomorphic("foo","bar")
False

Example 3:

>>> Solution().isIsomorphic("paper","title")
True

>>> Solution().isIsomorphic("bbbaaaba","aaabbbba")
False
"""
import doctest


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False
        return True


doctest.testmod()
