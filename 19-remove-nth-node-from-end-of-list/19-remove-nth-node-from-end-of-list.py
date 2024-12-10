class Solution:
    def removeNthFromEnd(self,head,n):
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head



# fast = ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}

# slow = ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
# fast = ListNode{val: 5, next: None}

# slow.next = ListNode{val: 4, next: ListNode{val: 5, next: None}}
# slow.next.next = ListNode{val: 5, next: None}

# slow = ListNode{val: 3, next: ListNode{val: 5, next: None}}