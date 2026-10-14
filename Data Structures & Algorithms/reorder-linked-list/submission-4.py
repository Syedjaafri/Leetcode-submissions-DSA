# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #only 4 parts

        # part 1 --> set the pointers and it's traversal
        slow = head
        fast = head.next

        
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        #part 2 --> now split the LL into two halves and find the middle 
        secondhalf = slow.next  # saving the head of the 2nd half , before None
        slow.next = None  #splitting happens
        prev = None

        #part 3 --> so it's time to reverse the second half
        # 8-->10-->None    to  10-->8-->None

        while secondhalf:
            temp = secondhalf.next  # store the next var , temp --> 10 
            secondhalf.next = prev  # at first iteration 8 --> none , because prev is none
            prev = secondhalf       # prev --> 8 --> none
            secondhalf = temp       # secondhalf = 10

        # at second iteration 
        # temp = 11
        # 10 --> 8 --> none  ans//
        # secondhalf = 11

        # at 3rd iteration none and not go inside the while loop 

        # PART 4 --> merge the reversed 2nd half with the 1st half alternatively , to get  the final output LINKEDLIST

        secondhalf = prev # doing this beacuse : at part3 , second half is none , we nee dto reset it to the prev , since prev is 10 , prev-->10 , so secondhalf->10
        while head and secondhalf:
            temp1 = head.next  
            temp2 = secondhalf.next

            head.next = secondhalf
            secondhalf.next = temp1
            head  = temp1   # new head is node 4 , which is temp1 , in the 1st iteration
            secondhalf = temp2  # now the new secondhalf's head is temp2 ,which is 8 
            # because to continue the next iteration of the while loop 





