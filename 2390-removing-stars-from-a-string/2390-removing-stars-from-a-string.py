class Solution:
    def removeStars(self,s):
        stack = []
        for i in s:
            if i == "*":
                stack.pop()
                continue
            stack.append(i)
        return "".join(stack)

obj = Solution()
print(obj.removeStars("leet**cod*e"))

