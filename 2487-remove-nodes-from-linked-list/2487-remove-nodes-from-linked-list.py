class Solution:
    def removeNodes(self,head):
        stack = []
        curr = head
        while curr:
            while stack and stack[-1] < curr.val:
                stack.pop()
            stack.append(curr.val)
            curr = curr.next

        dummy = ListNode()
        curr = dummy
        for val in stack:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next






# ListNode{val: 0, next: ListNode{val: 13, next: None}}
# ListNode{val: 0, next: ListNode{val: 13, next: None}}
# ListNode{val: 13, next: ListNode{val: 8, next: None}}
# ListNode{val: 0, next: ListNode{val: 13, next: ListNode{val: 8, next: None}}}
# ListNode{val: 13, next: ListNode{val: 8, next: None}}
# ListNode{val: 8, next: None}



