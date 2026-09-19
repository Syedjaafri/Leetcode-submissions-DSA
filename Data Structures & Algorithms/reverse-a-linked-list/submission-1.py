# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# recursive method

        if not head:  # there's no head , hence the list is null
            return None
            
        newhead  = head

        if head.next:
            newhead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newhead


