# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        count = 0 

        node = head
        #fill up stack 
        while node:
            stack.append(node)
            node = node.next
        
        threshold = len(stack) // 2

        while count != threshold:
            #save values
            tmp_next = head.next
            tail = stack.pop()

            #reorganize pointers
            head.next = tail
            tail.next = tmp_next

            #move forward
            head = tail.next
            count += 1
        
        head.next = None