"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # this one is to walk through the copy version 
        # this one is to walk through the original version
        # CLAUDE: I wonder, if this is the standard when you need to walk through a list
        # without alterning the pointers
        

        # i got a problem: the error is saying that the length are different 
        # i suspect that it caused by this while loop
        # i will trace by hand
        
        original_to_copy = dict()
        curr = head
        copy = None 
        copyCurr = copy
        while curr:
            copyCurr = Node(curr.val)
            original_to_copy[curr] = copyCurr
            if copy is None:
                copy = copyCurr
            curr = curr.next
        
        curr = head 
        copyCurr = copy
        
        while curr:
            if curr.next is not None:
                copyCurr.next = original_to_copy[curr.next]
            if curr.random is not None:
                copyCurr.random = original_to_copy[curr.random]
            copyCurr = copyCurr.next
            curr = curr.next
        # now that all the nodes exist 
        # i can make a pair key value dictionary 
    
        # the above while loop make the new copy of all the node in the original list
        # now i need to make the random pointer to point to the new 
        # the new copy called copy 
        # make another one to walk through this new copy 
        return copy


            
