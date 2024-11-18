class Solution:
    def moveZeroes(self,nums):
        l = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
        print(nums)
obj = Solution()
obj.moveZeroes([0,1,0,3,12]) 