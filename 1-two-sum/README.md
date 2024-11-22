
# Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Constrain

- 2 <= nums.length <= 104
- -109 <= nums[i] <= 109
- -109 <= target <= 109


## Example 1

```javascript
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]
```





### Solution: 

### Dry Run:
| **`i`** | **`j`** | **`nums[i]`** | **`nums[j]`** | **`nums[i] + nums[j]`** | **Condition (`== target`)** | **`arr`** |
|---------|----------|---------------|---------------|-------------------------|----------------------------|-----------|
| 0       | 1        | 2             | 7             | 9                       | True                       | `[[0, 1]]`|
| 0       | 2        | 2             | 11            | 13                      | False                      | `[[0, 1]]`|
| 0       | 3        | 2             | 15            | 17                      | False                      | `[[0, 1]]`|
| 1       | 2        | 7             | 11            | 18                      | False                      | `[[0, 1]]`|
| 1       | 3        | 7             | 15            | 22                      | False                      | `[[0, 1]]`|
| 2       | 3        | 11            | 15            | 26                      | False                      | `[[0, 1]]`|

### Final Result
The function returns `[[0,1]]`, which represents indices

