nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
nums1[:] = nums1[:len(nums1) - len(nums2)] + nums2
print(nums1.sort())
        
