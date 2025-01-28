class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_of_dict = {}

        for i, num in enumerate(nums):

            if num in num_of_dict:
                if abs(i - num_of_dict[num]) <= k:
                    return True

            num_of_dict[num] = i
            
        return False
