nums = [2,7,11,15]
target = 9

#  2+7 = 9
#  2+11 = 9
#  2+15 = 9

#  7=11 = 9
#  7=15 = 9

#  11+15 = 9

arr = []
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            arr.append([i,j])
print(arr)

