
# Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

## Constrain


- 1 <= nums.length <= 3 * 104
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order.

## Example 1

```javascript
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```



### Dry Run of `removeDuplicates` Function

The function iterates through the array, checking for duplicates and modifying the array in-place. Below is the step-by-step dry run in a table format:

| Step | `l` (left pointer) | `r` (right pointer) | `nums` array       | Action Taken           |
|------|---------------------|---------------------|--------------------|------------------------|
| 1    | 0                   | 1                   | `[1, 1, 2]`        | Duplicate found, pop `nums[1]` |
| 2    | 0                   | 1                   | `[1, 2]`           | No duplicate, increment `l` and `r` |
| 3    | 1                   | 2                   | `[1, 2]`           | End of array reached, return result |

### Explanation of Table

- **`l` (left pointer):** Tracks the position of the last unique element.
- **`r` (right pointer):** Scans the next element for duplicates.
- **`nums` array:** Reflects the state of the array after each operation.
- **Action Taken:** Describes what happens at each step (pop, increment, etc.).

### Final Output

The modified `nums` array is `[1, 2]`.

