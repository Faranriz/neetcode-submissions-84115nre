# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# [1,2,3,4,5]
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        second = dummy
        first = head
        for i in range(n):
            first = first.next
        
        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next
        




