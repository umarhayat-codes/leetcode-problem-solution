

# Square of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.



## Constrain

- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums is sorted in non-decreasing order.


## Example 1

```javascript

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

```





## Explanation in Table Form


| Index | Value Before Squaring | Value After Squaring | List State |
|-------|-----------------------|----------------------|------------|
| 0     | -4                   | 16                   | [16, -1, 3, 6, 10] |
| 1     | -1                   | 1                    | [16, 1, 3, 6, 10] |
| 2     | 3                    | 9                    | [16, 1, 9, 6, 10] |
| 3     | 6                    | 36                   | [16, 1, 9, 36, 10] |
| 4     | 10                   | 100                  | [16, 1, 9, 36, 100] |

After sorting: [1, 9, 16, 36, 100]


## Final Result

The final output of `sortedSquares([-4,-1,0,3,10])` is: [1, 9, 16, 36, 100].

