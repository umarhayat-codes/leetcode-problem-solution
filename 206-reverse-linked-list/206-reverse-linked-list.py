class Solution:
    def reverseLinkList(self,head):
        cur = head
        prev = None
        while cur.next:
            tempNext = cur.next 
            cur.next = prev
            prev = cur
            cur = tempNext
        return prev
    




# Dry Run in Link List form
# cur = ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
# tempNext = cur.next  =ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
# cur.next = prev | prev = None
# cur = ListNode{val: 1, next: None}
# pre = cur

# cur = tempNext = ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}

# tempNext = cur.next  = ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
# # cur.next = prev | prev = ListNode{val: 1, next: None}
# cur = ListNode{val: 2, next: ListNode{val: 1, next: None}}
# prev = cur

# cur = temNext = ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}

# tempNext = cur.next  = ListNode{val: 4, next: ListNode{val: 5, next: None}}
# cur.next = prev | prev = ListNode{val: 2, next: ListNode{val: 1, next: None}}
# cur = ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}
# prev = cur

# cur = tempNext = ListNode{val: 4, next: ListNode{val: 5, next: None}}

# tempNext = cur.next  = ListNode{val: 5, next: None}
# cur.next = prev | prev = ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}
# cur ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}
# prev = cur 

# cur = tempNExt = ListNode{val: 5, next: None}

# tempNExt = cur.next = None
# cur.next = prev | prev ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}
# cur = ListNode{val: 5, next: ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}}
# prev = cur
# cur = tempNExt = None


# ListNode{val: 5, next: ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}}




