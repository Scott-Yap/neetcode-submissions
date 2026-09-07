# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # two pointers, 1 normal, 1 starts n + 1 steps ahead
        # once reach the end the normal one would be at n + 1 from the back
        # then we skip the n one and connect to n - 1 from the back

        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # fast n + 1 ahead

        for i in range(n+1):
            fast = fast.next

        while fast: 
            slow = slow.next
            fast = fast.next

        # slow at the node before n 

        slow.next = slow.next.next

        return dummy.next
