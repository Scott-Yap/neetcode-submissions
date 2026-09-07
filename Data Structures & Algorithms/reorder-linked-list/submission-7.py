# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # split into two parts 
        if not head.next or not head.next.next:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next 
        slow.next = None

        reverse = second
        track = second.next 
        reverse.next = None
        
        
        # reverse second
        while track:
            current = track.next
            track.next = reverse
            reverse = track
            track = current


        # weave them together

        while head and reverse:

            head_next = head.next
            second_next = reverse.next

            head.next = reverse
            head = reverse
            reverse = second_next

            head.next = head_next
            head = head_next