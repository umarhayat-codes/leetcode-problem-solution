
# Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Constrain

- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.


## Example 1

```javascript
Input: s = "()[]{}"

Output: true
```



### Dry Run 


| Step | Character | Stack State         | Action                |
|------|-----------|---------------------|-----------------------|
| 1    | (         | ['(']              | Push '(' onto stack   |
| 2    | )         | []                 | Pop matching ')' from stack |
| 3    | [         | ['[']              | Push '[' onto stack   |
| 4    | ]         | []                 | Pop matching ']' from stack |
| 5    | {         | ['{']              | Push '{' onto stack   |
| 6    | }         | []                 | Pop matching '}' from stack |
| -    | -         | []                 | Final state: Valid    |



### Final Output

The check of string is valid become `True`.

