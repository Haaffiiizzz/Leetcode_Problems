# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        second = head

        while first and first.next:
            first = first.next.next
            second = second.next
        
        return second

#idea is to moveone twice as fast as another. once the first reaches the end, the second will be at the middle