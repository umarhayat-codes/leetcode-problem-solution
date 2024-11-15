
# Find All Anagram In String

Given two strings s and p, return an array of all the start indices of p's 
anagrams
 in s. You may return the answer in any order.
 

## Constrain


- 1 <= s.length, p.length <= 3 * 104
- s and p consist of lowercase English letters.

## Example 1

```
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

```



### Explanation By Table:

| Start Index | Substring from `s` | Is Anagram of `p`? |
|-------------|---------------------|--------------------|
| 0           | "cba"              | Yes                |
| 1           | "bae"              | No                 |
| 2           | "aeb"              | No                 |
| 3           | "eba"              | No                 |
| 4           | "bab"              | No                 |
| 5           | "aba"              | No                 |
| 6           | "bac"              | Yes                |

### Note:
- Substrings `"cba"` (start index = 0) and `"bac"` (start index = 6) are anagrams of `p = "abc"`.
- The output is `[0,6]`.


