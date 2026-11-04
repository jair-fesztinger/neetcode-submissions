# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        tracker = set()

        i = head

        while i: #can we compute the len / range of linked lists? 
            
            if not tracker: #when hash empty
                tracker.add(i)
            elif i in tracker: #if there is an existing value in hash map hence cycle
                return True
            else:
                tracker.add(i)

            i = i.next
        return False