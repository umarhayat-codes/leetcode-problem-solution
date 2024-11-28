
# Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their 
intersection
. Each element in the result must be unique and you may return the result in any order.



## Constrain

- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 1000

## Example 1

```javascript

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

```


| Step | i | nums1[i] | j | nums2[j] | Intersection | Action |
|------|---|----------|---|----------|--------------|--------|
| 1    | 0 | 1        | 0 | 2        | []           | Increment i |
| 2    | 1 | 2        | 0 | 2        | []           | Move both pointers, append 2 to intersection |
| 3    | 2 | 2        | 1 | 2        | [2]          | Increment i |

### Final Output

The modified `intersection` is `[2]`.

