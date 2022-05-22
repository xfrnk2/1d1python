from typing import ListNode, Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow
        return None
