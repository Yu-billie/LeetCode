# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        p1, p2 = l1, l2
        carry = 0

        while p1 is not None or p2 is not None:
            x = p1.val if p1 is not None else 0
            y = p2.val if p2 is not None else 0

            sum_val = x + y + carry
            carry = sum_val // 10

            current.next = ListNode(sum_val % 10)
            current = current.next

            if p1 is not None:
                p1 = p1.next
            if p2 is not None:
                p2 = p2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy_head.next

        
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


