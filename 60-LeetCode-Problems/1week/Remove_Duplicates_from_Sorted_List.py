from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        p = head

        while p.next:
            if p.next.val == p.val:
                p.next = p.next.next
            else:
                p = p.next

        return head
