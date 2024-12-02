

# Removing Stars From a String

You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.


## Constrain

- 1 <= s.length <= 105
- s consists of lowercase English letters and stars *.
- The operation above can be performed on s.




## Example 1

```javascript

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".

```





## Explanation in Table Form

| **Step** | **Character** | **Action**                               | **Stack**        |
|----------|---------------|------------------------------------------|------------------|
| 1        | `l`           | Add to stack                            | `['l']`          |
| 2        | `e`           | Add to stack                            | `['l', 'e']`     |
| 3        | `e`           | Add to stack                            | `['l', 'e', 'e']`|
| 4        | `t`           | Add to stack                            | `['l', 'e', 'e', 't']` |
| 5        | `*`           | Remove top of the stack (pop `t`)        | `['l', 'e', 'e']`|
| 6        | `*`           | Remove top of the stack (pop `e`)        | `['l', 'e']`     |
| 7        | `c`           | Add to stack                            | `['l', 'e', 'c']`|
| 8        | `o`           | Add to stack                            | `['l', 'e', 'c', 'o']`|
| 9        | `d`           | Add to stack                            | `['l', 'e', 'c', 'o', 'd']`|
| 10       | `*`           | Remove top of the stack (pop `d`)        | `['l', 'e', 'c', 'o']`|
| 11       | `e`           | Add to stack                            | `['l', 'e', 'c', 'o', 'e']`|



## Final Result

The final output of `removeStars('leet**cod*e')` is: `lecoe`.
