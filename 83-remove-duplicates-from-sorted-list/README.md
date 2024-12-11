

# 83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well

## Constrain


- The number of nodes in the list is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order.



## Example 1

```javascript

Input: head = [1,1,2,3,3]
Output: [1,2,3]

```



# Dry Run for `deleteDuplicates` Function

### Function Description:
The `deleteDuplicates` function removes duplicates from a sorted linked list.

### Dry Run Table:

Suppose we have the input linked list: `1 -> 1 -> 2 -> 3 -> 3`.

| Step | Current Node (`curr.val`) | Next Node (`curr.next.val`) | Action Taken                               | Updated Linked List    |
|------|---------------------------|----------------------------|-------------------------------------------|-------------------------|
| 1    | 1                         | 1                          | Duplicate found. Skip next node.          | 1 -> 2 -> 3 -> 3       |
| 2    | 1                         | 2                          | No duplicate. Move to the next node.      | 1 -> 2 -> 3 -> 3       |
| 3    | 2                         | 3                          | No duplicate. Move to the next node.      | 1 -> 2 -> 3 -> 3       |
| 4    | 3                         | 3                          | Duplicate found. Skip next node.          | 1 -> 2 -> 3            |
| 5    | 3                         | None                       | End of list reached. Stop iteration.      | 1 -> 2 -> 3            |

### Explanation:

- **Step 1**: The current node is `1`, and the next node is also `1`. Since the values are equal, skip the next node by updating `curr.next` to `curr.next.next`.
- **Step 2**: The current node is still `1`, and the next node is `2`. Move the `curr` pointer to the next node.
- **Step 3**: The current node is now `2`, and the next node is `3`. Move the `curr` pointer to the next node.
- **Step 4**: The current node is `3`, and the next node is also `3`. Skip the next node by updating `curr.next` to `curr.next.next`.
- **Step 5**: The current node is still `3`, and there is no next node. The iteration stops.

### Final Output:
The modified linked list is: `1 -> 2 -> 3`.
