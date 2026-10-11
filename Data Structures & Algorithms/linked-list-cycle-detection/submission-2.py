# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head   #both slow and fast starts from the head the begining node

        while fast and fast.next:
            
            slow = slow.next  # slow pointer moves each node

            fast = fast.next.next  # and fast point traverse by incrementing +2

            if slow == fast:  # ther's a cycle , since fast didn't end in none / null

                return True

        return False
