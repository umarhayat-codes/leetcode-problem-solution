s = "cbaebabacd"
p = "abc"
class Solution:
    def findAnagrams(self, s, p):
        arr = []
        p = sorted(p)
        for i in range(len(s) - len(p) + 1):
            window_sliding = sorted(s[i : len(p) + i])
            if p == window_sliding:
                arr.append(i)
        return arr
obj = Solution()
print(obj.findAnagrams(s,p))



# Time: 7088 ms (7.53%) | Memory: 17.26 MB (75.41%) - LeetSync