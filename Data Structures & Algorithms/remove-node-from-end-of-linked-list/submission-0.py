# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# [1,2,3,4,5]
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # len of head
        head1 = head
        count = 0
        while head1:
            head1 = head1.next
            count += 1
        # nth node from front (0 indexed)
        if count == n:
            return head.next
        n = count - n

        # remove nth node
        count = 0
        curr = head
        while curr:
            if count == n - 1:
                curr.next = curr.next.next
                return head
            curr = curr.next
            count += 1
        return head





