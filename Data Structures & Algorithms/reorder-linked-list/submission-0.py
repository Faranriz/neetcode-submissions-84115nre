# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 1,2,3,4
# 1,2,3,4,5
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split into two lists
        second = slow.next
        slow.next = None

        # reverse second half of list
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        second = prev
        # merge alternate first and second
        while second:
            tmp1, tmp2 = head.next, second.next
            head.next = second
            second.next = tmp1
            head, second = tmp1, tmp2

       

