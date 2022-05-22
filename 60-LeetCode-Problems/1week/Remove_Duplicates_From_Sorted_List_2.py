from typing import Optional


class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        # self.next = next


class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is None:
        return head
        #
        # first: Optional["ListNode"] = ListNode(0, head)
        # p: Optional["ListNode"] = first
        #
        # while head:
        #     if head.next and head.val == head.next.val:
        #         while head.next and head.val == head.next.val:
        #             head = head.next
        #         p.next = head.next
        #     else:
        #         p = p.next
        #
        #     head = head.next
        #
        # return first.next
