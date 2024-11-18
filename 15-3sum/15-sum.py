class Solution:
    def threeSum(self, nums): 
        nums.sort()
        Set = set()
        Arr = []
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    Set.add((nums[i] , nums[j] , nums[k]))
                    k -= 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
        for i in Set:
            Arr.append(i)
        print(Arr)
        return Arr

obj = Solution()
print(obj.threeSum([-1,0,1,2,-1,-4]))
