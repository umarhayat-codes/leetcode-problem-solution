

# Minimum String Length After Removing Substrings

You are given a string s consisting only of uppercase English letters.

You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.

Return the minimum possible length of the resulting string that you can obtain.

Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.

## Constrain

- 1 <= s.length <= 100
- s contains only lower and upper case English letters.


## Example 1

```javascript
Input: s = "ABFCACDB"
Output: 2
Explanation: We can do the following operations:
- Remove the substring "ABFCACDB", so s = "FCACDB".
- Remove the substring "FCACDB", so s = "FCAB".
- Remove the substring "FCAB", so s = "FC".
So the resulting length of the string is 2.
It can be shown that it is the minimum length that we can obtain.
```





## Explanation in Table Form
| Step | Current Character (`i`) | Stack Before | Action Taken                  | Stack After |
|------|--------------------------|--------------|-------------------------------|-------------|
| 1    | A                        | []           | Push 'A'                      | [A]         |
| 2    | B                        | [A]          | Pop 'A' and discard 'B'       | []          |
| 3    | F                        | []           | Push 'F'                      | [F]         |
| 4    | C                        | [F]          | Push 'C'                      | [F, C]      |
| 5    | A                        | [F, C]       | Push 'A'                      | [F, C, A]   |
| 6    | C                        | [F, C, A]    | Push 'C'                      | [F, C, A, C]|
| 7    | D                        | [F, C, A, C] | Pop 'C' and discard 'D'       | [F, C, A]   |
| 8    | B                        | [F, C, A]    | Pop 'A' and discard 'B'       | [F, C]      |

## Final Result

The final output of `minLength('ABFCACDB')` is: 2.

