

# Make The String Great

Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.


## Constrain

- 1 <= s.length <= 100
- s contains only lower and upper case English letters.


## Example 1

```javascript
Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""i = 2, both will result "abBAcC" to be reduced to "".

```





## Explanation in Table Form

| Step | Current Char | Operation                  | Stack          |
|------|--------------|---------------------------|----------------|
| 1    | a            | Add 'a' to stack          | a              |
| 2    | b            | Add 'b' to stack          | ab             |
| 3    | B            | Remove 'b' and 'B' (opposites) | a              |
| 4    | A            | Remove 'a' and 'A' (opposites) |                |
| 5    | c            | Add 'c' to stack          | c              |
| 6    | C            | Remove 'c' and 'C' (opposites) |                |
|      |              | Final Result: `''.join(stack)` |                |


## Final Result

The final output of `makeGood('abBAcC')` is: ``.

