
# Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

## Constrain


- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -109 <= nums1[i], nums2[j] <= 109

## Example 1

```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1
```


## Code Explanation

1. **Initialize Indices**:
   - `i = m - 1`: Points to the last element in the populated part of `nums1`.
   - `j = n - 1`: Points to the last element in `nums2`.
   - `k = m + n - 1`: Points to the last position in `nums1` where merged elements will be placed.

2. **Looping through elements**:
   - The `while` loop continues as long as there are elements in `nums2` (`j >= 0`).
   - Inside the loop:
     - If `i >= 0` (there are elements left in `nums1`) and `nums1[i] > nums2[j]`, the larger element (`nums1[i]`) is placed in position `k`, and `i` and `k` are decremented.
     - Otherwise, `nums2[j]` is placed in position `k`, and `j` and `k` are decremented.

3. **Decrement `k`**: Ensures we are filling `nums1` from the end towards the beginning.



### Step-by-Step Table

| Step | `i` | `j` | `k` | `nums1[i]` | `nums2[j]` | Comparison              | `nums1` after step        |
|------|-----|-----|-----|------------|------------|-------------------------|---------------------------|
| Init | 2   | 2   | 5   | 3          | 6          | -                       | `[1, 2, 3, 0, 0, 0]`      |
| 1    | 2   | 2   | 5   | 3          | 6          | `nums1[i] < nums2[j]`   | `[1, 2, 3, 0, 0, 6]`      |
| 2    | 2   | 1   | 4   | 3          | 5          | `nums1[i] < nums2[j]`   | `[1, 2, 3, 0, 5, 6]`      |
| 3    | 2   | 0   | 3   | 3          | 2          | `nums1[i] > nums2[j]`   | `[1, 2, 3, 3, 5, 6]`      |
| 4    | 1   | 0   | 2   | 2          | 2          | `nums1[i] <= nums2[j]`  | `[1, 2, 2, 3, 5, 6]`      |
| 5    | 1   | -1  | 1   | 2          | -          | `j < 0` (loop ends)     | `[1, 2, 2, 3, 5, 6]`      |

### Final Result

After all steps, `nums1` becomes `[1, 2, 2, 3, 5, 6]`, which is the merged sorted array.