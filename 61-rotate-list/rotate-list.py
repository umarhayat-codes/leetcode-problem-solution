# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        arr = []
        curr = head
        
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        k = k % len(arr)
        if k == 0:
            return head
        arr = arr[-k: ] + arr[ :-k]
        
        dummy = ListNode()
        tail = dummy
        for val in arr:
            tail.next = ListNode(val)
            tail = tail.next
        
        return dummy.next