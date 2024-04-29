"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""

def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        done = []
        
        curr = head
        while curr:
            if curr.val not in done:
                done.append(curr.val)
                prev = curr
                curr = curr.next  
            else:
                prev.next = curr.next
                curr = curr.next
        return head   