# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        track = head.next 
        result = head
        result.next = None

        while track:
            next_node = track.next 
            track.next = result
            result = track
            track = next_node
        
        return result