
# Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
 

## Constrain


- 1 <= nums.length <= 10^4
- -231 <= nums[i] <= 2^31 - 1

## Example 1

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

```




### Step-by-Step Table

| **Iteration** | **Index (i)** | **nums[i]** | **Left Pointer (l)** | **Action**                                              | **Array State**   |
|---------------|---------------|-------------|-----------------------|--------------------------------------------------------|-------------------|
| Start         | -             | -           | 0                     | Initial state                                          | `[0, 1, 0, 3, 12]` |
| 1             | 0             | 0           | 0                     | Zero, so no action                                     | `[0, 1, 0, 3, 12]` |
| 2             | 1             | 1           | 0                     | Swap `nums[l]` and `nums[i]`, then `l += 1`           | `[1, 0, 0, 3, 12]` |
| 3             | 2             | 0           | 1                     | Zero, so no action                                     | `[1, 0, 0, 3, 12]` |
| 4             | 3             | 3           | 1                     | Swap `nums[l]` and `nums[i]`, then `l += 1`           | `[1, 3, 0, 0, 12]` |
| 5             | 4             | 12          | 2                     | Swap `nums[l]` and `nums[i]`, then `l += 1`           | `[1, 3, 12, 0, 0]` |
| End           | -             | -           | -                     | Final array after all iterations                      | `[1, 3, 12, 0, 0]` |
"""
### Final Result

After all steps, `nums` becomes `[1,3,12,0,0]`.