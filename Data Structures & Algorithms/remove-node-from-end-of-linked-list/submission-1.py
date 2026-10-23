# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # approach 1 : array brute force approach 

        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next

        index = len(arr) - n

        if index == 0:
            
            return head.next

    
        arr[index -1].next = arr[index].next
        arr[index].next= None
        return head


