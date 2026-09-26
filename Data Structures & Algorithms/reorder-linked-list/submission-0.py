# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):6
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # low and fast pointer to only find the midpoint 
        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # find 2nd half        
        l2 = slow.next
        # l1 = slow 
        prev = slow.next = None

        while l2:
            nxt = l2.next
            l2.next = prev
            prev = l2
            l2 = nxt

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1, tmp2 