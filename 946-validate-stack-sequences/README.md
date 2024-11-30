

# Validate Stack Sequences

Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.




## Constrain

- 1 <= pushed.length <= 1000
- 0 <= pushed[i] <= 1000
- All the elements of pushed are unique.
- popped.length == pushed.length
- popped is a permutation of pushed.



## Example 1

```javascript

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

```




### Dry Run of `validateStackSequences` Method

#### Input
- **pushed**: [1, 2, 3, 4, 5]
- **popped**: [4, 5, 3, 2, 1]

#### Explanation Table

| Step | Current `pushed` Element | Stack          | `popped[i]` | Action                        | i   |
|------|---------------------------|----------------|-------------|-------------------------------|-----|
| 1    | 1                         | [1]            | 4           | Push 1 onto stack             | 0   |
| 2    | 2                         | [1, 2]         | 4           | Push 2 onto stack             | 0   |
| 3    | 3                         | [1, 2, 3]      | 4           | Push 3 onto stack             | 0   |
| 4    | 4                         | [1, 2, 3, 4]   | 4           | Push 4 onto stack             | 0   |
| 5    | -                         | [1, 2, 3]      | 5           | Pop 4 from stack, increment i | 1   |
| 6    | -                         | [1, 2]         | 3           | Pop 5 from stack, increment i | 2   |
| 7    | -                         | [1]            | 2           | Pop 3 from stack, increment i | 3   |
| 8    | -                         | []             | 1           | Pop 2 from stack, increment i | 4   |
| 9    | -                         | []             | -           | All elements processed        | 5   |

#### Final Check
- The stack is empty: **True**
- Return: **True**
