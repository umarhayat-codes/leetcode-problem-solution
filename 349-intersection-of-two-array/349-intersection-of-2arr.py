class Solution:
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        i,j = 0,0
        intersection = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j] and nums1[i] not in intersection:
                intersection.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return intersection
    
obj = Solution()
print(obj.intersection([1,2,2,1],[2,2]))
