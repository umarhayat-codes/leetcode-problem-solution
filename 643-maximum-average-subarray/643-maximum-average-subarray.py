class Solution:
    def findMaxAverage(self, nums, k):
        cur_sum = sum(nums[:k])
        max_sum = cur_sum
        for i in range(k,len(nums)):
            cur_sum += nums[i]
            cur_sum -= nums[i-k]
            max_sum = max(max_sum,cur_sum)
        max_avg = max_sum / k
        return max_avg 
obj = Solution()
print(obj.findMaxAverage([1,12,-5,-6,50,3],4))