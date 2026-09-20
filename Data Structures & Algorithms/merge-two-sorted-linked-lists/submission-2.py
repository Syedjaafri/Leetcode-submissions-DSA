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


        syed = []  # temp list to store the sorted list

        curr1 = list1
        while curr1:
            syed.append(curr1.val)  # appending operations of list1 to syed list
            curr1 = curr1.next      # incrementing the list's pointer

        curr2 = list2
        while curr2:
            syed.append(curr2.val)   # appending operations of list2 to syed list
            curr2 = curr2.next
        
        # sorting 
        syed.sort()  # [1,1,2,3,4,5]

        dummy = ListNode()  # Creates an empty starting node.
        current = dummy     # both pointer points empty(0) pointing node, where current traverse and moves forward and dummy stays in fixed position

        for val in syed:  
            current.next = ListNode(val) # adding the elements one by one
            current = current.next       # for incrementing and adding  consecutively
        return dummy.next                # the currrent  nodes stored in dummy , so returning dummy.next

        

        