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
            
        newhead  = head  # storing the current head in the newhead variable

        if head.next:    # if the head has the next node / element, go inside the condition
            newhead = self.reverseList(head.next) # RECURSION CALLING FUNCTION , this function waits,until the next functions give the answers to it(giving the head.next paramenter , i.e incrementing the head, nodes , to reverse the linked list)
            head.next.next = head   # the actual pointer manipulation happens
        head.next = None     # after pointer manipulation , breaking the existing pointer to avoid loop
        return newhead  # finally printing the all answers from all the recursive calls and returing


