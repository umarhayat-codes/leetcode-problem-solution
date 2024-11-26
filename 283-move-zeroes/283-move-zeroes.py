# class Solution:
#     def moveZeroes(self,nums):
#         l = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[l], nums[i] = nums[i], nums[l]
#                 l += 1
#         print(nums)
# obj = Solution()
# obj.moveZeroes([0,1,0,3,12]) 


class Solution:
    def moveZeroes(self,nums):
        left = 0
        for right in range(1,len(nums)):
            if nums[left] != 0:
                left += 1 
                continue
            if nums[right] != 0:
                nums[left] ,nums[right] = nums[right] ,nums[left]
                left += 1
        return nums
obj = Solution()
print(obj.moveZeroes([0,1,0,3,12]))




