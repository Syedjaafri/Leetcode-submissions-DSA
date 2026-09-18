# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head

        while curr:
            nxt = curr.next  # store the next node , when we change pointer in the nxt line

            curr.next = prev # changing the pointer of the curr , from next to pre

            prev = curr # incrementing the prev

            curr = nxt  # incremening the curr 

        return prev  # it has chain of 4 nodes[0,1,2,3]
        