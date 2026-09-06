# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        track = head

        while track and track.next:

            head = head.next
            track = track.next.next
            if head == track:
                return True
    
        return False