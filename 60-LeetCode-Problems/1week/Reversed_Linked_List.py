from typing import Any, List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        stack: List[Any] = [0]
        while head:
            stack.append(head)
            head = head.next

        current = stack.pop()
        final = current
        while stack:
            current.next = stack.pop()
            if stack:
                current = current.next
            else:
                current.next = None

        return final
