# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        
        n1, n2 = 0, 0
        
        
        square_l1 = square_l2 = 0
        
        while l1:
            n1 += l1.val * 10 ** square_l1
            square_l1 += 1
            l1 = l1.next
        while l2:
            n2 += l2.val * 10 ** square_l2
            square_l2 += 1
            l2 = l2.next
        
        res = list(str(n1 + n2))

        
        last_node = ListNode(res[0], None)
        for i in range(1, len(res)):
            current_node = ListNode(res[i], last_node)
            last_node = current_node
        
        return last_node