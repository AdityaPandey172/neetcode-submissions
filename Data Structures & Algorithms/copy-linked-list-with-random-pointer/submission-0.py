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
        if not head:
            return None
        
        current = head
        while current:
            duplicate = Node(current.val)
            duplicate.next = current.next
            current.next = duplicate
            current = duplicate.next

        current = head 
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        original = head
        duplicate_head = head.next
        current = duplicate_head
        while original:
            original.next = original.next.next
            if current.next:
                current.next = current.next.next
            original = original.next
            current = current.next
        
        return duplicate_head
