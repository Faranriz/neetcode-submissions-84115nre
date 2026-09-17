# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# [0,1,2,3]
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            next_node = curr.next #ref to node 2 from node 1
            curr.next = prev #ref to next node reversed
            prev = curr #move prev pointer forward
            curr = next_node #move curr pointer to next node
        return prev