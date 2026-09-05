# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # head = 0 ,1 ,2 ,3, none
        # track = 1,2,3
        # result 0 , none

        # 0, none , none

        if not head:
            return head
            
        track_node = head.next
        result = head 

        result.next = None

        while track_node:
            next_node = track_node.next   # save forward
            track_node.next = result      # reverse arrow
            result = track_node           # move result forward
            track_node = next_node        # move to unreversed part

        return result
