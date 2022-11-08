"""
Given the head of a singly linked list, group all the nodes with odd indices
together followed by the nodes with even indices, and return
the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain
as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time
complexity.

Example 1:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
"""
from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head

        oddpointer = head
        evenpointer = head.next
        evenhead = evenpointer
        current = head
        i = 1

        while current:
            if i > 2 and i % 2 != 0:
                oddpointer.next = current
                oddpointer = oddpointer.next
            elif i > 2 and i % 2 == 0:
                evenpointer.next = current
                evenpointer = evenpointer.next
            current = current.next
            i += 1
        evenpointer.next = None
        oddpointer.next = evenhead

        return head
