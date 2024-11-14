
# Maximum Average Subarray

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

## Constrain


- n == nums.length
- 1 <= k <= n <= 105
- -104 <= nums[i] <= 104

## Example 1

```
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
```



### Table Breakdown:

| Index `i` | `Window` (Current subarray)   | `cur_sum` (Current sum) | `max_sum` (Maximum sum) | Reason |
|-----------|-------------------------------|-------------------------|-------------------------|--------|
| 0         | [1, 12, -5, -6]               | 1 + 12 + (-5) + (-6) = 2  | 2                       | First sum of the first k elements |
| 1         | [12, -5, -6, 50]              | 2 + 50 - 1 = 51         | 51                      | Slide window, add 50, remove 1 |
| 2         | [-5, -6, 50, 3]               | 51 + 3 - 12 = 42        | 51                      | Slide window, add 3, remove 12 |
| 3         | [-6, 50, 3, -5]               | 42 + (-5) - (-5) = 42   | 51                      | Slide window, add -5, remove -5 |
| 4         | [50, 3, -5, -6]               | 42 + (-6) - (-6) = 42   | 51                      | Slide window, add -6, remove -6 |

### Final Calculation:
- The maximum sum found is `51`.
- The maximum average is `51 / 4 = 12.75`.
