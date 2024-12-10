

# Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.



## Constrain


- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz


## Example 1

```javascript

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

```



### Dry Run for removeNthFromEnd Function

#### Linked List: `1 -> 2 -> 3 -> 4 -> 5`, n = 2

| Step | Operation                  | slow  | fast  | Comment                                 |
|------|----------------------------|-------|-------|-----------------------------------------|
| 1    | Initialize pointers        | 1     | 1     | Both `slow` and `fast` start at head    |
| 2    | Move `fast` forward `n`    | 1     | 3     | Move `fast` 2 steps ahead               |
| 3    | Check if `fast` is None    | 1     | 3     | `fast` is not None, proceed             |
| 4    | Move `slow` and `fast`     | 2     | 4     | Both `slow` and `fast` move one step    |
| 5    | Move `slow` and `fast`     | 3     | 5     | Both `slow` and `fast` move one step    |
| 6    | Move `slow` and `fast`     | 4     | None  | `fast` reaches the end, stop iteration  |
| 7    | Modify `slow.next`         | 4     | None  | Remove the nth node (`5`)              |
| 8    | Return head                | 1     | None  | Modified list: `1 -> 2 -> 3 -> 4`      |

## Final Result

The final output of `1 -> 2 -> 3 -> 4 -> 5` is: `1 -> 2 -> 3 -> 5`.
