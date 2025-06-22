class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        all_num_sum = int(n * (n + 1) / 2)
        present_num_sum = sum(nums)
        missing_num = all_num_sum - present_num_sum
        return missing_num 