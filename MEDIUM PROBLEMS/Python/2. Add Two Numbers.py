# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digit1 = []
        digit2 = []

        while l1 or l2:
            if l1:
                digit1.insert(0, str(l1.val))
                l1 = l1.next
            
            if l2:
                digit2.insert(0, str(l2.val))
                l2 = l2.next

        digit1 = int("".join(digit1))
        digit2 = int("".join(digit2))
        result = str(digit1 + digit2)
        result = result[::-1]

        new = ListNode()
        current = new

        for char in result:
            current.next = ListNode(int(char))
            current = current.next

        return new.next
