# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # brute force approach 
        # adding both lists to values list , by traversing and appending
        # sorting tht values list ,
        # creating a dummy new linked list with it's pointer current
        # ListNode(val) with next nos of curr.next
        # returning that newly created dummy LL


        syed = []

        curr1 = list1
        while curr1:
            syed.append(curr1.val)
            curr1 = curr1.next

        curr2 = list2
        while curr2:
            syed.append(curr2.val)
            curr2 = curr2.next
        
        # sorting 
        syed.sort()

        dummy = ListNode()
        current = dummy

        for val in syed:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

        

        