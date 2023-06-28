# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional 
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> ListNode:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            merged = list1
            merged.next = self.mergeTwoLists(list1.next, list2)
        else:
            merged = list2
            merged.next = self.mergeTwoLists(list1, list2.next)

        return merged


# Creating example linked lists using ListNode method 
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

s = Solution()
result = s.mergeTwoLists(list1, list2)

# Printing the merged linked list
while result:
    print(result.val, end=" ")
    result = result.next