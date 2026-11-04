# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        hash = {}

        i = head

        while i: #can we compute the len / range of linked lists? 
            
            if not hash: #when hash empty
                hash[i] = 'Si'
            elif i in hash: #if there is an existing value in hash map hence cycle
                return True
            else:
                hash[i] = 'Si'

            i = i.next
        return False