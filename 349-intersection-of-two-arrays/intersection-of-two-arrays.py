class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        unique_item = []

        while i < len(nums1) and j < len(nums2):
        
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                if nums1[i] not in unique_item:
                    unique_item.append(nums1[i])
                i +=1
                j +=1

        return unique_item