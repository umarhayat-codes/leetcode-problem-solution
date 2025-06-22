class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_arr = sorted(nums)
        mid_item = n // 2
        return sorted_arr[mid_item]
