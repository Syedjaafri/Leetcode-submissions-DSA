# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # BRUTE FORCE APPROACH , POINTER MODIFICATION , CREATING A NEW LIST AND STORING THE LINKED LISTS IN LIST FORMAT

        if not head:  # check for if the LL / head is empty
            return

        reorder = []  # creating a list for stoing the values
        curr = head   # storing the head in the curr var

        while curr:
            reorder.append(curr) #adding elements one by one in the reoder list
            curr = curr.next

        i = 0                   
        j = len(reorder) - 1 # i pointer from 0 , j pointer starts at the last of the reorder list

        while i < j:
            reorder[i].next = reorder[j]  #changing the i pointer nodes
            i = i + 1                     #increment

            if i >= j:  # both pointer was in the middle index , then there's no nodes balance to modify , because we using the 2 pointer approach 
                break

            reorder[j].next = reorder[i]   # changing the j pointer nodes
            j = j - 1                      # decrement

        reorder[i].next = None            # if the loop breaks/ends , the last i pointer will point the None


            



