class Solution:
    def sortedSquares(self,nums):
#       1. Approach

        for i in range(len(nums)):
            nums[i] *= nums[i]        
        return sorted(nums)


#       2. Approach

        # square_num = []
        # for i in nums:
        #     square_num.append(i ** 2)
        # return sorted(square_num)


#       3. Approach

        # i = 0
        # while i < len(nums):
        #     nums[i] *= nums[i]
        #     i += 1
        # return sorted(nums)


obj = Solution()
print(obj.sortedSquares([-4,-1,3,6,10]))

