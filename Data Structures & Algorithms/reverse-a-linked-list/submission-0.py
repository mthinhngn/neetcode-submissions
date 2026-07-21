# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


# Pre vid:
# make a loop to count how many in an array to run the loop
# then push it many time
# 3-> 2-> 1. 3 times, so run the loop 3 times

# Diff approach:    
# 2 pointer: point to each link then reverse it

        prev, curr = None, head

        while curr: 
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev