

# Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

## Constrain

- The number of nodes in the list is in the range [1, 105].
- 0 <= Node.val <= 9


## Example 1

```javascript


Input: head = [1,2,2,1]
Output: true

```








## Dry Run for `isPalindrome` Function

Suppose the linked list is `1 -> 2 -> 2 -> 1`.

| Step | Current Node Value (`curr.val`) | Array (`arr`)        | Comment                          |
|------|---------------------------------|----------------------|----------------------------------|
| 1    | 1                               | `[1]`               | Append `1` to `arr`.            |
| 2    | 2                               | `[1, 2]`            | Append `2` to `arr`.            |
| 3    | 2                               | `[1, 2, 2]`         | Append `2` to `arr`.            |
| 4    | 1                               | `[1, 2, 2, 1]`      | Append `1` to `arr`.            |
| 5    | `None`                          | `[1, 2, 2, 1]`      | Reached the end of the list.    |
| 6    | -                               | `arr == arr[::-1]`  | Check if the array is a palindrome. Result: `True`. |

# Final Result:
`1 -> 2 -> 2 -> 1 -> True`

