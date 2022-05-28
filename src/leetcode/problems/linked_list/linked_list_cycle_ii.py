from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode], pos: int) -> str:
        fast = slow = head

        while fast is not None and fast.next is not None:
            slow = slow.next  # type: ignore
            fast = fast.next.next

            if slow == fast:

                slow = head
                while slow != fast:
                    slow = slow.next  # type: ignore
                    fast = fast.next  # type: ignore

                return f"tail connects to node index {pos}"
        return "no cycle"
