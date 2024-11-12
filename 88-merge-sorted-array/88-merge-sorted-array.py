# 1. approach
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
nums1[:] = nums1[:len(nums1) - len(nums2)] + nums2
print(nums1.sort())
        


# 2. appraach
m = 3
n = 3
i = m - 1
j = n - 1
k = len(nums1) - 1
while j <= 0:
        if i <= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
        else:
                nums1[k] = nums2[j]
                j -= 1
        k -= 1

