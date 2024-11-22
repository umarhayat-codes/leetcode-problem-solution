
# Three Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
## Constrain


- 3 <= nums.length <= 3000
- -105 <= nums[i] <= 105


## Example 1

```javascript

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

```





### Solution: 
| **`i` (index)** | **`nums[i]`** | **`j` (index)** | **`nums[j]`** | **`k` (index)** | **`nums[k]`** | **`total`** | **Action**                                                                 | **`Set`**                     |
|------------------|---------------|-----------------|---------------|-----------------|---------------|-------------|-----------------------------------------------------------------------------|--------------------------------|
| 0                | -4            | 1               | -1            | 5               | 2             | -3          | Total < 0 → Increment `j`                                                  | `{}`                           |
| 0                | -4            | 2               | -1            | 5               | 2             | -3          | Total < 0 → Increment `j`                                                  | `{}`                           |
| 0                | -4            | 3               | 0             | 5               | 2             | -2          | Total < 0 → Increment `j`                                                  | `{}`                           |
| 0                | -4            | 4               | 1             | 5               | 2             | -1          | Total < 0 → Increment `j`                                                  | `{}`                           |
| 1                | -1            | 2               | -1            | 5               | 2             | 0           | Total == 0 → Add `(-1, -1, 2)` to `Set`, Decrement `k`                     | `{(-1, -1, 2)}`                |
| 1                | -1            | 2               | -1            | 4               | 1             | -1          | Total < 0 → Increment `j`                                                  | `{(-1, -1, 2)}`                |
| 1                | -1            | 3               | 0             | 4               | 1             | 0           | Total == 0 → Add `(-1, 0, 1)` to `Set`, Decrement `k`                     | `{(-1, -1, 2), (-1, 0, 1)}`    |
| 2                | -1            | 3               | 0             | 5               | 2             | 1           | Total > 0 → Decrement `k`                                                  | `{(-1, -1, 2), (-1, 0, 1)}`    |
| 3                | 0             | 4               | 1             | 5               | 2             | 3           | Total > 0 → Decrement `k`                                                  | `{(-1, -1, 2), (-1, 0, 1)}`    |

### Final Result
The function returns '[[-1,-1,2],[-1,0,1]]' 

