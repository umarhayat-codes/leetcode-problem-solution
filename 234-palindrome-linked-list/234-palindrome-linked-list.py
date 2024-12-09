class Solution:
    def isPalindrome(self,head):
        arr = []
        curr = head
        while curr is not None:
            arr.append(curr.val)
            curr = curr.next
        return arr == arr[::-1]
    


# Dry Run in link list form

# ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}
# 1

# ListNode{val: 2, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}
# 2

# ListNode{val: 2, next: ListNode{val: 1, next: None}}
# 2

# ListNode{val: 1, next: None}
# 1

 