# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from leetcode import ListNode


class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        dict = {}
        while p is not None :
            if dict.get(p.val) is None:
                dict[p.val] = 0

            dict[p.val] = 1 + dict[p.val]
            p = p.next

        result = ListNode(0)
        p = result
        for key, value in dict.items():
            node = ListNode(value)
            p.next = node
            p = p.next

        return result.next



