

# Remove Nodes From Linked List

You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

## Constrain

- The number of the nodes in the given list is in the range [1, 10^5].
- 1 <= Node.val <= 10^5




## Example 1

```javascript

Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.

```




## Dry Run of `removeNodes`

Given the input linked list: `5 -> 2 -> 13 -> 3  -> 8 `

| Step | Current Node (`curr.val`) | Stack Before Operation | Action                   | Stack After Operation | Dummy Linked List |
|------|----------------------------|-------------------------|--------------------------|------------------------|-------------------|
| 1    | 5                          | []                      | Append `5`              | [5]                   |                   |
| 2    | 2                          | [5]                     | Append `2`              | [5, 2]                |                   |
| 3    | 13                         | [5, 2]                  | Pop `2`, Pop `5`, Append `13` | [13]                  |                   |
| 4    | 3                          | [13]                    | Append `3`              | [13, 3]               |                   |
| 5    | 8                          | [13, 3]                 | Pop `3`, Append `8`     | [13, 8]               |                   |

After the stack is constructed, we rebuild the linked list:
- Resulting linked list: `[13, 8]`

### Final Dummy Linked List Creation Steps

| Step | Value Added to Linked List | Dummy Linked List State |
|------|-----------------------------|--------------------------|
| 1    | 13                          | 13 ->                   |
| 2    | 8                           | 13 -> 8 ->              |


## Final Result

The final output of `5 -> 2 -> 13 -> 3  -> 8` is: `13 -> 8 -> `.
