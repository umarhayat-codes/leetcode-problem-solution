class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        if n == 1:
            return nums
        
        even_idx = 0
        for i in range(n):
            if nums[i] % 2 == 0:
                nums[even_idx],nums[i] = nums[i], nums[even_idx]
                even_idx += 1
        
        return nums
