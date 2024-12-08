

# Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

## Constrain

- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000


## Example 1

```javascript


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

```









# Dry Run Table for reverseLinkList Function

| **Step** | **cur** (Current Node)                     | **tempNext** (Next Node)                     | **cur.next** (Reversed Link)                           | **prev** (Previous Node)                               | **Updated cur**                   |
|----------|-------------------------------------------|----------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-----------------------------------|
| 1        | `1 -> 2 -> 3 -> 4 -> 5`                  | `2 -> 3 -> 4 -> 5`                          | `None`                                               | `1 -> None`                                         | `2 -> 3 -> 4 -> 5`               |
| 2        | `2 -> 3 -> 4 -> 5`                       | `3 -> 4 -> 5`                               | `1 -> None`                                           | `2 -> 1 -> None`                                      | `3 -> 4 -> 5`                    |
| 3        | `3 -> 4 -> 5`                            | `4 -> 5`                                    | `2 -> 1 -> None`                                      | `3 -> 2 -> 1 -> None`                                 | `4 -> 5`                         |
| 4        | `4 -> 5`                                 | `5`                                         | `3 -> 2 -> 1 -> None`                                 | `4 -> 3 -> 2 -> 1 -> None`                            | `5`                              |
| 5        | `5`                                      | `None`                                      | `4 -> 3 -> 2 -> 1 -> None`                            | `5 -> 4 -> 3 -> 2 -> 1 -> None`                       | `None`                           |

# Final Result:
`5 -> 4 -> 3 -> 2 -> 1 -> None`

