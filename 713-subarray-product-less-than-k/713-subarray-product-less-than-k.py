class Solution:
    def  numSubarrayProductLessThanK(self,nums,k):

        if k < 1:
            return 0
        
        left = 0
        res = 0
        product = 1
        for right in range(len(nums)):
            product = product * nums[right]

            while product >= k and left <= right:
                product = product // nums[left]
                left += 1
            res += right - left + 1
        return res

obj = Solution()
print(obj.numSubarrayProductLessThanK([10,5,2,6],100))


