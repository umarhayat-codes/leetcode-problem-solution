class Solution:
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        intersection = []
        i,j = 0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersection.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return intersection

obj = Solution()
print(obj.intersect([4,9,5],[9,4,9,8,4]))


        