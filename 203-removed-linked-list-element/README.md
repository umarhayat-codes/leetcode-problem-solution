

# Remove Linked List Elements

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.


## Constrain


- The number of nodes in the list is in the range [0, 104].
- 1 <= Node.val <= 50
- 0 <= val <= 50




## Example 1

```javascript

Example 1:

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4],

```





## Explanation in Table Form

### Dry Run of `removeElements` Function

| Step | Current Node Value | Next Node Value | Action |
|------|--------------------|-----------------|--------|
| 1    | 0                  | 1               | Move to next node |
| 2    | 1                  | 2               | Move to next node |
| 3    | 2                  | 6               | Remove node with value 6 |
| 4    | 2                  | 3               | Move to next node |
| 5    | 3                  | 4               | Move to next node |
| 6    | 4                  | 5               | Move to next node |
| 7    | 5                  | 6               | Remove node with value 6 |
| 8    | 5                  | None            | Move to next node |


## Final Result

The final output of `removeElement('ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 6, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: ListNode{val: 6, next: None}}}}}}}')` is: `ListNode{val: 1, next: ListNode{val: 2,  next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, ,next : None}}}}}`.
