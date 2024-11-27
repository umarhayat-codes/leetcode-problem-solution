

# Subarray Product Less Than K

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.




## Constrain



- 1 <= nums.length <= 3 * 104
- 1 <= nums[i] <= 1000
- 0 <= k <= 106


## Example 1

```javascript

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

```





## Explanation in Table Form



| Iteration | Right Pointer | Product      | Left Pointer | Subarrays Counted | Res |
|-----------|---------------|--------------|--------------|-------------------|-----|
| 1         | 0             | 10           | 0            | 1                 | 1   |
| 2         | 1             | 50           | 0            | 2                 | 3   |
| 3         | 2             | 100          | 1            | 2                 | 5   |
| 4         | 3             | 60           | 1            | 3                 | 8   |


## Final Result

The final output of `numSubarrayProductLessThanK([10,5,2,6])` is: 8.

